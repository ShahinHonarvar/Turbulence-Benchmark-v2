from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_count = 0
    for anagram_group in anagram_dict.values():
        if len(anagram_group) >= 2:
            anagram_count += len(anagram_group) * (len(anagram_group) - 1) // 2
    return anagram_count >= 7