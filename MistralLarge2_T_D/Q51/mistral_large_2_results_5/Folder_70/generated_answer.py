from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagram_count[key] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_count.values() if v > 1))
    return anagram_pairs <= 97