from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagram_dict[sorted_word].append(word)
    anagram_pairs = sum((1 for group in anagram_dict.values() if len(group) >= 2))
    return anagram_pairs >= 194