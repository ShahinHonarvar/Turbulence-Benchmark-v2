from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_dict[''.join(sorted(word.lower()))].append(word)
    anagram_count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_count >= 136