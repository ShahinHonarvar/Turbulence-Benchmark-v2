from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_count = 0
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_map[sorted_word].append(word)
    for key, value in anagram_map.items():
        if len(value) > 1:
            anagram_count += len(value) * (len(value) - 1) // 2
    return anagram_count >= 73