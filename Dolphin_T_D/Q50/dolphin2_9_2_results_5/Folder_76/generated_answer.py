def if_contains_anagrams(lst):
    pairs = 0
    for word1 in lst:
        for word2 in lst:
            if len(word1) >= 3 and len(word2) >= 3 and (word1 != word2) and (sorted(word1.lower()) == sorted(word2.lower())):
                pairs += 1
                if pairs == 143:
                    return True
    return pairs >= 143