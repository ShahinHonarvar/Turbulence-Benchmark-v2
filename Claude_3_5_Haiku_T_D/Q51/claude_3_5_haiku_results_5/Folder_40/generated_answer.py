def if_contains_anagrams(word_list):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_pairs = 0
    n = len(word_list)
    for i in range(n):
        for j in range(i + 1, n):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3:
                if is_anagram(word_list[i], word_list[j]):
                    anagram_pairs += 1
                    if anagram_pairs > 29:
                        return False
    return True