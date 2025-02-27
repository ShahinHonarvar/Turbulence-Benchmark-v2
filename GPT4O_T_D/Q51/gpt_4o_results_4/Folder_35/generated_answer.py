from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_buckets = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            anagram_buckets[normalized].append(s)
    for bucket in anagram_buckets.values():
        n = len(bucket)
        if n >= 2:
            anagram_count += n * (n - 1) // 2
    return anagram_count <= 210