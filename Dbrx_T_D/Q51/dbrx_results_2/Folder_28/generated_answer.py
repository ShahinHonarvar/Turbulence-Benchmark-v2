def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(word) >= 3:
            anagrams[sorted_word] = anagrams.get(sorted_word, 0) + 1
    anagram_pairs = sum((count // 2 for count in anagrams.values()))
    return anagram_pairs <= 78