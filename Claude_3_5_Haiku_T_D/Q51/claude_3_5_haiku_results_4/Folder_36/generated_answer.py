def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def is_valid_anagram_pair(word1, word2):
        return len(word1) >= 3 and len(word2) >= 3 and (word1.lower() != word2.lower()) and is_anagram(word1, word2)
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_valid_anagram_pair(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 25:
                    return False
    return True