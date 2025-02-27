from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        processed_word = ''.join(sorted(word.lower()))
        if len(processed_word) >= 3:
            anagram_map[processed_word].append(word)
    anagram_pairs = 0
    for group in anagram_map.values():
        n = len(group)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
        if anagram_pairs > 60:
            return False
    return True