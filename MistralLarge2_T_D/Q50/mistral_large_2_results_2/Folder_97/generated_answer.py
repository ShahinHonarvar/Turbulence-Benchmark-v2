from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    pair_count = 0
    for string in strings:
        if len(string) < 3:
            continue
        normalized = normalize(string)
        pair_count += anagram_count[normalized]
        anagram_count[normalized] += 1
    return pair_count >= 123