from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            anagram_counts[sorted_s] += 1
    pair_count = 0
    for count in anagram_counts.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
            if pair_count > 89:
                return False
    return True