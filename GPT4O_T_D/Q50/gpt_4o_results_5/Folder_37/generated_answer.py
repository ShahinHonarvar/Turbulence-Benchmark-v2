from collections import defaultdict

def if_contains_anagrams(words):
    word_map = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_map[sorted_word] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in word_map.values()))
    return anagram_pairs >= 29