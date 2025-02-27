def if_contains_anagrams(lst):
    anagrams = 0
    for word1 in lst:
        for word2 in lst:
            if word1.lower() != word2.lower() and len(word1) >= 3 and (len(word2) >= 3):
                sorted_word1 = sorted(word1.lower())
                sorted_word2 = sorted(word2.lower())
                if sorted_word1 == sorted_word2:
                    anagrams += 1
    return anagrams // 2 >= 108