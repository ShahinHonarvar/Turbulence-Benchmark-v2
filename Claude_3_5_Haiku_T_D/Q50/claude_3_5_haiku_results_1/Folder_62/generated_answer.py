def if_contains_anagrams(word_list):
    anagram_pairs = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            word1 = word_list[i].lower()
            word2 = word_list[j].lower()
            if len(word1) >= 3 and len(word2) >= 3 and (sorted(word1) == sorted(word2)):
                anagram_pairs += 1
    return anagram_pairs >= 43