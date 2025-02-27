from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    anagram_map = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word] += 1
    for count in anagram_map.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 35:
                return False
    return True