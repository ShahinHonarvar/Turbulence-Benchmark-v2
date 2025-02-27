def if_contains_anagrams(lst):
    count = 0
    for word1 in lst:
        if len(word1) >= 3 and word1.lower() not in set(word1.lower()):
            for word2 in lst:
                if len(word2) >= 3 and word2.lower() not in set(word2.lower()) and (sorted(word1.lower()) == sorted(word2.lower())) and (word1.lower() != word2.lower()):
                    count += 1
                    if count >= 28:
                        return True
    return False