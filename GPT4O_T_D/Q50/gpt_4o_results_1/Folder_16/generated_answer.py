from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_chars(s):
        return ''.join(sorted(s.lower()))
    count = 0
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sort_chars(s)
            anagram_map[sorted_s].append(s)
    for anagram_list in anagram_map.values():
        n = len(anagram_list)
        count += n * (n - 1) // 2
        if count >= 155:
            return True
    return False