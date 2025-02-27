from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_tuple(word):
        return tuple(sorted(word.lower()))
    anagram_map = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagram_map[sorted_tuple(word)] += 1
    count = 0
    for value in anagram_map.values():
        if value > 1:
            count += value * (value - 1) // 2
    return count >= 314