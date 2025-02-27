from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_dict[''.join(sorted(word.lower()))].append(word)
    anagram_count = sum([len(val) * (len(val) - 1) // 2 for val in anagram_dict.values() if len(val) >= 2])
    return anagram_count >= 14