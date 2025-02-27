def if_contains_anagrams(lst):
    anagrams = 0
    for word1 in lst:
        for word2 in lst:
            if word1 != word2 and len(word1) >= 3 and (len(word2) >= 3):
                if sorted(word1.lower()) == sorted(word2.lower()):
                    anagrams += 1
    return anagrams >= 89