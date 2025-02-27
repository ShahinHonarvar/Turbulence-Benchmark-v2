def if_contains_anagrams(lst):
    count = 0
    for word1 in lst:
        for word2 in lst:
            if len(word1) >= 3 and len(word2) >= 3 and (word1.lower() != word2.lower()) and (sorted(word1.lower()) == sorted(word2.lower())):
                count += 1
    return count >= 276