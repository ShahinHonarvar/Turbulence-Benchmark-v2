from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_dict[canonical_form(word)].append(word)
    anagram_pairs = [len(list(combinations(group, 2))) for group in anagram_dict.values() if len(group) > 1]
    return sum(anagram_pairs) <= 60