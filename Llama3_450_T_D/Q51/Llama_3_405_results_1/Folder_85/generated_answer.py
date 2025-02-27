from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_pairs = 0
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            sorted_string = ''.join(sorted(string.lower()))
            anagrams[sorted_string].append(string)
    for value in anagrams.values():
        length = len(value)
        anagram_pairs += length * (length - 1) // 2
        if anagram_pairs > 276:
            return False
    return True