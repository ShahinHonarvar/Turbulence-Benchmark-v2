def if_contains_anagrams(lst):
    counter = 0
    for word1 in lst:
        if len(word1) < 3:
            continue
        for word2 in lst:
            if len(word2) < 3 or word1 == word2:
                continue
            if sorted(word1.lower()) == sorted(word2.lower()):
                counter += 1
    return counter >= 69