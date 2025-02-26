def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        word1 = ''.join(sorted(word1.lower()))
        word2 = ''.join(sorted(word2.lower()))
        return word1 == word2 and len(word1) >= 3
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 91:
                    return False
    return True