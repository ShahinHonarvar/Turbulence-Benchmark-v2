def if_contains_anagrams(lst):
    count_pairs = 0
    for word1 in lst:
        if len(word1) >= 3:
            for word2 in lst:
                if len(word2) >= 3:
                    if sorted(word1.lower()) == sorted(word2.lower()) and word1 != word2:
                        count_pairs += 1
                        break
    return count_pairs // 2 >= 59