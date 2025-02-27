from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_counts = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_counts[sorted_word].append(word)
    anagram_pairs = 0
    for group in anagram_counts.values():
        n = len(group)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 257