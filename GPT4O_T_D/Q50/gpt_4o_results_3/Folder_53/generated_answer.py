from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word] += 1
    count = 0
    for key in anagram_map:
        if anagram_map[key] > 1:
            pairs = anagram_map[key] * (anagram_map[key] - 1) // 2
            count += pairs
            if count >= 11:
                return True
    return False