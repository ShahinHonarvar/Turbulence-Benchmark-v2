import collections

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    count = collections.Counter()
    for s in strings:
        if len(s) < 3:
            continue
        count[canonical_form(s)] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values() if v > 1))
    return anagram_pairs <= 11