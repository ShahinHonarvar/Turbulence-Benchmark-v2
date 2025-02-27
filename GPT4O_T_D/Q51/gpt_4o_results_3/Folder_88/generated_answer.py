from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(int)
    words = [word.lower() for word in words]
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word] += 1
    anagram_pairs = 0
    for count in anagram_map.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 407