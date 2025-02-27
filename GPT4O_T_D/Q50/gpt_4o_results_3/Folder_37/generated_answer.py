from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word] += 1
    anagram_pairs_count = 0
    for count in anagram_map.values():
        if count > 1:
            anagram_pairs_count += count * (count - 1) // 2
    return anagram_pairs_count >= 29