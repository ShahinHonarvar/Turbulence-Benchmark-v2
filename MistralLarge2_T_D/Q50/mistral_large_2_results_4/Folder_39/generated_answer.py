from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            can_form = canonical_form(s)
            anagram_count[can_form].append(s)
    pairs_count = 0
    for anagrams in anagram_count.values():
        if len(anagrams) >= 2:
            pairs_count += len(anagrams) * (len(anagrams) - 1) // 2
    return pairs_count >= 54