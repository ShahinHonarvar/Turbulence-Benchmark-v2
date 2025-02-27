from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_map.values() if count > 1))
    return anagram_pairs <= 423