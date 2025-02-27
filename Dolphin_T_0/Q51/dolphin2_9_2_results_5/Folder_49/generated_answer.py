def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            word1 = lst[i].lower()
            word2 = lst[j].lower()
            if len(word1) < 3 or len(word2) < 3:
                continue
            if sorted(word1) == sorted(word2):
                count += 1
                if count > 10:
                    return False
    return count <= 10