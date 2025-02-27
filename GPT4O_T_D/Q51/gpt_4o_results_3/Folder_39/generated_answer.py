from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    anagram_pairs = 0
    for words in anagram_map.values():
        if len(words) > 1:
            n = len(words)
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs > 257:
                return False
    return True