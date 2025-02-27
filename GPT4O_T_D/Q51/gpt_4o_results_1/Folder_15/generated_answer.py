from collections import defaultdict

def if_contains_anagrams(words):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    anagram_groups = defaultdict(set)
    for word in words:
        if len(word) >= 3:
            key = canonical_form(word)
            anagram_groups[key].add(word.lower())
    anagram_pairs_count = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return anagram_pairs_count <= 20