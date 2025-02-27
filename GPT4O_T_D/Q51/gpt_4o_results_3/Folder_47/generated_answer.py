from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_map = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_map[normalized_word] += 1
    count = 0
    for _, freq in anagram_map.items():
        if freq > 1:
            count += freq * (freq - 1) // 2
    return count <= 366