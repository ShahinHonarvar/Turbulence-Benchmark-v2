def if_contains_anagrams(lst):
    counter = 0
    for i, word1 in enumerate(lst):
        for j in range(i + 1, len(lst)):
            word2 = lst[j]
            if len(word1) >= 3 and len(word2) >= 3 and (sorted(word1.lower()) == sorted(word2.lower())):
                counter += 1
                if counter >= 42:
                    return True
    return False