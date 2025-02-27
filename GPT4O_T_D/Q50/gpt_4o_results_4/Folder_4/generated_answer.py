from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word.lower())
    anagram_pairs = 0
    for group in anagrams.values():
        if len(group) > 1:
            n = len(group)
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs >= 42:
                return True
    return anagram_pairs >= 42