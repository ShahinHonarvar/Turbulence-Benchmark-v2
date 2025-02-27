from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagram_count[key].append(s)
    count_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_count.values()))
    return count_pairs <= 257