def if_contains_anagrams(words):
    word_anagram_map = {}
    for word in words:
        word_sorted = ''.join(sorted(word.lower()))
        if len(word_sorted) >= 3:
            word_anagram_map[word_sorted] = word_anagram_map.get(word_sorted, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in word_anagram_map.values()))
    return anagram_pairs <= 73