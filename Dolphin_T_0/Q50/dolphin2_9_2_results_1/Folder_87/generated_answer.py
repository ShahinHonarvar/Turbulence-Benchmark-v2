def if_contains_anagrams(lst):
    count = sum((1 for word1, word2 in zip(lst, lst[1:]) if sorted(word1.lower()) == sorted(word2.lower()) and len(word1) >= 3 and (len(word2) >= 3)))
    return count >= 88