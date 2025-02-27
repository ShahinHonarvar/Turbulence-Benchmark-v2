from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            canon = canonical_form(string)
            anagram_map[canon].append(string)
    anagram_pairs = 0
    for word_list in anagram_map.values():
        n = len(word_list)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs >= 189