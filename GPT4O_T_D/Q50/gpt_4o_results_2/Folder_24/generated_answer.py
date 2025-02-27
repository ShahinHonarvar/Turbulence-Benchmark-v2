from collections import Counter

def if_contains_anagrams(words):
    anagram_map = Counter()
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word] += 1
    anagram_pairs = 0
    for count in anagram_map.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs >= 65:
                return True
    return False