from collections import defaultdict

def if_contains_anagrams(word_list):
    anagram_dict = defaultdict(list)
    for word in word_list:
        if len(word) >= 3:
            sorted_word = tuple(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_pairs = sum((1 for group in anagram_dict.values() if len(group) > 1))
    return anagram_pairs >= 68