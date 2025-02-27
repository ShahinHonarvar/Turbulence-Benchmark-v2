def if_contains_anagrams(lst):
    count = 0
    length = len(lst)
    for i in range(length):
        word1 = lst[i].lower()
        for j in range(i + 1, length):
            word2 = lst[j].lower()
            if len(word1) >= 3 and len(word2) >= 3 and (sorted(word1) == sorted(word2)):
                count += 1
                if count > 77:
                    return False
    return True