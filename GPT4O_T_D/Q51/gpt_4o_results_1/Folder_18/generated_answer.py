from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(int)
    for word in words:
        clean_word = ''.join(filter(str.isalpha, word)).lower()
        if len(clean_word) >= 3:
            sorted_word = ''.join(sorted(clean_word))
            anagram_map[sorted_word] += 1
    anagram_pairs = 0
    for count in anagram_map.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 42:
                return False
    return True