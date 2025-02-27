from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            anagram_dict[''.join(sorted(string.lower()))].append(string)
    anagram_count = sum((len(group) * (len(group) - 1) // 2 for group in anagram_dict.values()))
    return anagram_count >= 50