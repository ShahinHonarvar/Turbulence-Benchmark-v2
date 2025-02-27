from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    anagram_pairs = 0
    for anagrams in anagram_map.values():
        n = len(anagrams)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 401