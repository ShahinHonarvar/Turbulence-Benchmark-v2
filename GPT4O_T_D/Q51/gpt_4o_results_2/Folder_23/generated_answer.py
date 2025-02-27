from collections import defaultdict

def if_contains_anagrams(strings):

    def to_sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = to_sorted_lower(s)
            anagram_count[sorted_str] += 1
    anagram_pairs = 0
    for count in anagram_count.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 49:
                return False
    return True