def if_contains_anagrams(lst):
    ana_pairs = 0
    for word1 in lst:
        if len(word1) >= 3:
            for word2 in lst:
                if len(word2) >= 3 and word1 != word2:
                    if sorted(word1.lower()) == sorted(word2.lower()):
                        ana_pairs += 1
    if ana_pairs >= 106:
        return True
    else:
        return False