def if_contains_anagrams(lst):
    result = []
    for word1 in lst:
        for word2 in lst:
            if len(word1) >= 3 and len(word2) >= 3 and (sorted(word1.lower()) == sorted(word2.lower())):
                result.append([word1, word2])
    return len(result) >= 194