def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        word1 = ''.join(sorted(word1.lower()))
        word2 = ''.join(sorted(word2.lower()))
        return word1 == word2

    def is_valid_anagram(word1, word2):
        return len(word1) >= 3 and len(word2) >= 3 and is_anagram(word1, word2)
    anagram_count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_valid_anagram(words[i], words[j]):
                anagram_count += 1
                if anagram_count > 366:
                    return False
    return True