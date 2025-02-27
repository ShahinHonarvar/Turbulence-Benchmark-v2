def if_contains_anagrams(words):
    anagram_pairs = 0
    for i, word1 in enumerate(words):
        if len(word1) >= 3:
            for j in range(i + 1, len(words)):
                word2 = words[j]
                if len(word2) >= 3:
                    word1 = word1.lower()
                    word2 = word2.lower()
                    if sorted(word1) == sorted(word2):
                        anagram_pairs += 1
    return anagram_pairs >= 39