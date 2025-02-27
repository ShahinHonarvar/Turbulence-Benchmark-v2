from collections import defaultdict

def if_contains_anagrams(words):
    word_map = defaultdict(int)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            word_map[sorted_word] += 1
    anagram_pairs_count = sum((count // 2 for count in word_map.values()))
    return anagram_pairs_count >= 3