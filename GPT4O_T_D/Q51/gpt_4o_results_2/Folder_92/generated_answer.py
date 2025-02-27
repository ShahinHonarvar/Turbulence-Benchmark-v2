from collections import defaultdict

def if_contains_anagrams(words):
    word_map = defaultdict(int)
    for word in words:
        sorted_chars = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            word_map[sorted_chars] += 1
    anagram_pairs = sum((val * (val - 1) // 2 for val in word_map.values() if val > 1))
    return anagram_pairs <= 34