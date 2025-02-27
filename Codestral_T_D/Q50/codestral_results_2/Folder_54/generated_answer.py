def if_contains_anagrams(words):
    word_counts = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            word_counts[sorted_word] = word_counts.get(sorted_word, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in word_counts.values()))
    return anagram_pairs >= 74