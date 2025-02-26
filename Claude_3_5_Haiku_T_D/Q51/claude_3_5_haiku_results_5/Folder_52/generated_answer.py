def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        word1 = ''.join((char.lower() for char in word1 if char.isalpha()))
        word2 = ''.join((char.lower() for char in word2 if char.isalpha()))
        return len(word1) >= 3 and len(word2) >= 3 and (sorted(word1) == sorted(word2))
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 43:
                    return False
    return True