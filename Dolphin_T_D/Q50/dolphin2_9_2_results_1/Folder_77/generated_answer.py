def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            word1 = lst[i].lower()
            word2 = lst[j].lower()
            if len(word1) < 3 or len(word2) < 3:
                continue
            word1_sorted = ''.join(sorted(word1))
            word2_sorted = ''.join(sorted(word2))
            if word1_sorted == word2_sorted:
                count += 1
            if count >= 209:
                return True
    return False