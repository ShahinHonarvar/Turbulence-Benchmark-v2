from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word_tuple = tuple(sorted(word.lower()))
        anagram_dict[sorted_word_tuple].append(word)
    anagram_count = sum((1 for group in anagram_dict.values() if len(group) >= 2))
    return anagram_count >= 20