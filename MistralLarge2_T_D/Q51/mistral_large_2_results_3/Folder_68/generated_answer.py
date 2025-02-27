from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_count = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_count[sorted_word] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return anagram_pairs <= 94