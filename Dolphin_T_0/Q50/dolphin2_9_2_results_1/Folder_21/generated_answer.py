def if_contains_anagrams(lst):
    anagrams = 0
    for word1 in lst:
        if len(word1) >= 3:
            for word2 in lst:
                if len(word2) >= 3 and sorted(word1.lower()) == sorted(word2.lower()):
                    anagrams += 1
                    lst.remove(word2)
                    break
    return anagrams >= 136