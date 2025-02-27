def if_contains_anagrams(lst):
    count = 0
    for word1 in lst:
        if len(word1) >= 3:
            for word2 in lst:
                if len(word2) >= 3 and word1 != word2:
                    if sorted(word1.lower()) == sorted(word2.lower()):
                        count += 1
                        if count >= 177:
                            return True
    return False