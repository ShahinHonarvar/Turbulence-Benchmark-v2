from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            normal = normalize(word)
            anagram_count[normal] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pair_count <= 276