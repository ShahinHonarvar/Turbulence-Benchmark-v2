from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            anagram_count[sorted_str(s)] += 1
    pair_count = 0
    for count in anagram_count.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
            if pair_count > 68:
                return False
    return True