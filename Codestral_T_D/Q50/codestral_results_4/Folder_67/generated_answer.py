from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            anagrams_dict[''.join(sorted(string.lower()))].append(string)
    anagram_pairs = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagrams_dict.values()))
    return anagram_pairs >= 41