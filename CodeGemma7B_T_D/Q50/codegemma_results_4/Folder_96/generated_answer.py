from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    pairs = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) > 1:
            pairs += len(combinations(anagram_list, 2))
    return pairs >= 98