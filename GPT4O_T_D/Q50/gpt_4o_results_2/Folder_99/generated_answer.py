from collections import defaultdict

def if_contains_anagrams(words):
    count_anagrams = 0
    anagram_map = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            normalized = ''.join(sorted(word.lower()))
            anagram_map[normalized] += 1
    for count in anagram_map.values():
        if count > 1:
            count_anagrams += count * (count - 1) // 2
    return count_anagrams >= 314