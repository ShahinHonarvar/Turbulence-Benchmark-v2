from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            count[normalized] += 1
    anagram_pairs = 0
    for freq in count.values():
        if freq > 1:
            anagram_pairs += freq * (freq - 1) // 2
            if anagram_pairs >= 143:
                return True
    return False