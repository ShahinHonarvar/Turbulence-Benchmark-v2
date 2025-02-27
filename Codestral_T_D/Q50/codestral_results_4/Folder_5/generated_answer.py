from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for key in anagram_dict:
        anagram_pairs += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_pairs >= 21