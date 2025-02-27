from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagrams = defaultdict(list)
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        anagrams[sorted_string].append(string)
    anagram_pairs = sum((1 for value in anagrams.values() if len(value) >= 2))
    return anagram_pairs <= 86