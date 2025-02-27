from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_map[sorted_word] += 1
    count = 0
    for value in anagram_map.values():
        if value > 1:
            count += value * (value - 1) // 2
        if count > 93:
            return False
    return True