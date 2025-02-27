def if_contains_anagrams(lst):
    count = 0
    for word1, word2 in zip(lst, lst[1:]):
        if len(word1) >= 3 and len(word2) >= 3 and (sorted(word1.lower()) == sorted(word2.lower())):
            count += 1
    return count >= 74