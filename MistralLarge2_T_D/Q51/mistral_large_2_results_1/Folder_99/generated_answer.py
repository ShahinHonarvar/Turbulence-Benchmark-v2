from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            count[normalized] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs <= 93