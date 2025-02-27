from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = sorted_str(s)
            anagram_map[key].append(s)
    count = 0
    for group in anagram_map.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
        if count >= 69:
            return True
    return False