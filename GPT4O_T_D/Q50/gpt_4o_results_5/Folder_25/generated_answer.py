from collections import defaultdict

def if_contains_anagrams(words):
    word_map = defaultdict(int)
    for word in words:
        low_word = word.lower()
        if len(low_word) >= 3:
            sorted_word = ''.join(sorted(low_word))
            word_map[sorted_word] += 1
    count_pairs = sum((c * (c - 1) // 2 for c in word_map.values()))
    return count_pairs >= 14