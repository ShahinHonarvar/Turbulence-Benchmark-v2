def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_pairs = 0
    length = len(words)
    for i in range(length):
        for j in range(i + 1, length):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and is_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 8:
                    return False
    return True