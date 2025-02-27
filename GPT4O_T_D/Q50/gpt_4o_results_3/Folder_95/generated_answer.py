from collections import defaultdict

def if_contains_anagrams(words):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_map[canonical_form(word)].append(word)
    count_pairs = 0
    for word_list in anagram_map.values():
        n = len(word_list)
        if n > 1:
            count_pairs += n * (n - 1) // 2
        if count_pairs >= 93:
            return True
    return False