from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word] += 1
    count = 0
    for value in anagram_map.values():
        if value > 1:
            count += value * (value - 1) // 2
    return count <= 445