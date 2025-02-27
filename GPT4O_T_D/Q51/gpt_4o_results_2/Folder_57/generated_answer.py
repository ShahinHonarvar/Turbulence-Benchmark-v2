from collections import defaultdict

def if_contains_anagrams(words):

    def canonical_form(word):
        return ''.join(sorted(word))
    anagram_groups = defaultdict(list)
    count_pairs = 0
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            canon = canonical_form(word_lower)
            anagram_groups[canon].append(word_lower)
    for group in anagram_groups.values():
        if len(group) >= 2:
            n = len(group)
            count_pairs += n * (n - 1) // 2
            if count_pairs > 74:
                return False
    return True