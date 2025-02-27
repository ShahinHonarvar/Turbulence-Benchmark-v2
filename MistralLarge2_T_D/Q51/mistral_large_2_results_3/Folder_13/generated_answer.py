from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = set()
    counts = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        counts[sorted_s] += 1
    for count in counts.values():
        if count > 1:
            anagram_pairs.add((min(count, 54), count * (count - 1) // 2))
    total_pairs = sum((pair[1] for pair in anagram_pairs))
    return total_pairs <= 54