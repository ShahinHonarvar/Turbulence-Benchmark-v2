from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagrams = defaultdict(list)
    for string in string_list:
        sorted_string = sorted(string.lower() if len(string) >= 3 else '')
        anagrams[''.join(sorted_string)].append(string)
    for value in anagrams.values():
        if len(value) > 1:
            anagram_count += len(value) * (len(value) - 1)
    return anagram_count >= 44