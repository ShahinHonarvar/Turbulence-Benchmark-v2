def if_contains_anagrams(word_list):

    def is_anagram(word1, word2):
        return len(word1) >= 3 and len(word2) >= 3 and (sorted(word1.lower()) == sorted(word2.lower()))
    anagram_count = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if is_anagram(word_list[i], word_list[j]):
                anagram_count += 1
                if anagram_count >= 123:
                    return True
    return False