def if_contains_anagrams(str_list):
    anagram_pairs = 0
    for i, word1 in enumerate(str_list):
        for j, word2 in enumerate(str_list[i + 1:]):
            if len(word1) >= 3 and len(word2) >= 3 and (word1.lower() == word2.lower()):
                anagram_pairs += 1
    return anagram_pairs >= 233