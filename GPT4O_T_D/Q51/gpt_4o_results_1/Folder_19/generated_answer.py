from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_map[sorted_string].append(string)
    for anagrams in anagram_map.values():
        n = len(anagrams)
        if n > 1:
            anagram_count += n * (n - 1) // 2
            if anagram_count > 69:
                return False
    return True