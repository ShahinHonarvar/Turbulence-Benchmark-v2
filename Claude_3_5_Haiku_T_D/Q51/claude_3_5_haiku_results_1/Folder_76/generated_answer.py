def if_contains_anagrams(word_list):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_pairs = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3:
                if is_anagram(word_list[i], word_list[j]):
                    anagram_pairs += 1
                    if anagram_pairs > 91:
                        return False
    return True