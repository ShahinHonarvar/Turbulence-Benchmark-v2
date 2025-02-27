from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(int)
    count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            anagram_map[sorted_s] += 1
    for key in anagram_map:
        if anagram_map[key] > 1:
            count += anagram_map[key] * (anagram_map[key] - 1) // 2
            if count >= 21:
                return True
    return False