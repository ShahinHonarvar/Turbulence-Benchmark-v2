def if_contains_anagrams(word_list):

    def is_anagram(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        return sorted(word1) == sorted(word2)
    anagrams = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3 and is_anagram(word_list[i], word_list[j]):
                anagrams += 1
                if anagrams >= 20:
                    return True
    return False