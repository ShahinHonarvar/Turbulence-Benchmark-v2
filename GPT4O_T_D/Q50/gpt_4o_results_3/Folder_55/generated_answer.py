from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    sorted_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_map[sorted_str(s)] += 1
    for count in sorted_map.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count >= 15:
                return True
    return False