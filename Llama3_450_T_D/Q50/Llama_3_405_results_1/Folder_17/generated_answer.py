def if_contains_anagrams(words):
    anagram_counts = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_counts[sorted_word] = anagram_counts.get(sorted_word, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 97