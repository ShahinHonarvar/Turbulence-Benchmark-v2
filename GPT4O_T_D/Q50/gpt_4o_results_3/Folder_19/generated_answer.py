from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_pairs_count = 0
    normalized_anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            normalized_anagrams[sorted_word].append(word)
    for words in normalized_anagrams.values():
        n = len(words)
        if n > 1:
            anagram_pairs_count += n * (n - 1) // 2
    return anagram_pairs_count >= 84