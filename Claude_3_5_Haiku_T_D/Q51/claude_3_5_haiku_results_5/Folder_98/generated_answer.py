def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        if len(word1) < 3 or len(word2) < 3:
            return False
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_count += 1
                if anagram_count > 46:
                    return False
    return True