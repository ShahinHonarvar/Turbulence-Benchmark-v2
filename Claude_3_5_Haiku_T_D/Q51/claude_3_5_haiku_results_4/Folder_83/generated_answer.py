def if_contains_anagrams(word_list):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_count = 0
    n = len(word_list)
    for i in range(n):
        for j in range(i + 1, n):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3 and is_anagram(word_list[i], word_list[j]):
                anagram_count += 1
                if anagram_count > 19:
                    return False
    return True