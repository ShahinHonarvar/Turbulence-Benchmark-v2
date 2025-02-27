def if_contains_anagrams(lst):
    counter = 0
    for word1 in lst:
        if len(word1) >= 3:
            for word2 in lst:
                if len(word2) >= 3 and word1.lower() != word2.lower() and (sorted(word1.lower()) == sorted(word2.lower())):
                    counter += 1
                    if counter >= 194:
                        return True
    return False