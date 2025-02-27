from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    sorted_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = sort_string(s)
            sorted_map[sorted_str] += 1
    for count in sorted_map.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 47:
                return False
    return anagram_count <= 47