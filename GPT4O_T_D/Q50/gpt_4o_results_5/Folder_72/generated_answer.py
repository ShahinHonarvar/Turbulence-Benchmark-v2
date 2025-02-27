from collections import defaultdict

def if_contains_anagrams(words):
    word_map = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            word_map[sorted_word].append(word)
    anagram_pairs = 0
    for word_list in word_map.values():
        n = len(word_list)
        anagram_pairs += n * (n - 1) // 2
        if anagram_pairs >= 55:
            return True
    return False