from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    counts = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        counts[sorted_str] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in counts.values()))
    return anagram_pairs <= 10