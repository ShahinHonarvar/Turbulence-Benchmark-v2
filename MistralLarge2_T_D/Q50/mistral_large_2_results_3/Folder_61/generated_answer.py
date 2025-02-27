from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_pairs = [comb for comb in combinations(words, 2) if sorted(comb[0].lower()) == sorted(comb[1].lower()) and len(comb[0]) >= 3 and (len(comb[1]) >= 3)]
    return len(anagram_pairs) >= 8