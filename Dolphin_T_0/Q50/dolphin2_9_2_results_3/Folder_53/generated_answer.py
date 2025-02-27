def if_contains_anagrams(lst):
    count = 0
    for word1 in lst:
        for word2 in lst:
            if len(word1) >= 3 and len(word2) >= 3 and (sorted(word1.lower()) == sorted(word2.lower())):
                count += 1
                if count >= 11:
                    return True
    return False