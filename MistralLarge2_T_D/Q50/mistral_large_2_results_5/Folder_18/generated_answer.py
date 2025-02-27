from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    pair_count = 0
    for s in strings:
        if len(s) < 3:
            continue
        norm = normalize(s)
        pair_count += anagram_count[norm]
        anagram_count[norm] += 1
    return pair_count >= 106