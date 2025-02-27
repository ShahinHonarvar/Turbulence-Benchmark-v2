from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagram_count[key] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pairs <= 206