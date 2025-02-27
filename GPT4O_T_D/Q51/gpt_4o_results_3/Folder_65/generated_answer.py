from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(words):

    def sorted_key(word):
        return ''.join(sorted(word.lower()))
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_groups[sorted_key(word)].append(word)
    anagram_pairs_count = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            num_words = len(group)
            anagram_pairs_count += num_words * (num_words - 1) // 2
            if anagram_pairs_count > 72:
                return False
    return True