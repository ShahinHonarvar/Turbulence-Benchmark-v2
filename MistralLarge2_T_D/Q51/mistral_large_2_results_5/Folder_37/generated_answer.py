from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    pair_count = 0
    for s in strings:
        if len(s) >= 3:
            cf = canonical_form(s)
            pair_count += anagram_count[cf]
            anagram_count[cf] += 1
    return pair_count <= 206