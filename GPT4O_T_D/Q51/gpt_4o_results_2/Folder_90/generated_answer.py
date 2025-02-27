def if_contains_anagrams(words):
    counts = {}
    anagram_pairs = 0
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagram_pairs += counts.get(sorted_word, 0)
            counts[sorted_word] = counts.get(sorted_word, 0) + 1
        if anagram_pairs > 147:
            return False
    return True