def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def is_valid_anagram(word1, word2):
        return len(word1) >= 3 and len(word2) >= 3 and word1.isalpha() and word2.isalpha() and (word1.lower() != word2.lower())
    anagram_pairs = 0
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if is_valid_anagram(words[i], words[j]) and is_anagram(words[i], words[j]):
                anagram_pairs += 1
    return anagram_pairs <= 318