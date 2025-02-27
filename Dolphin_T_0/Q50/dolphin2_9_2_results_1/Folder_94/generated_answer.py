def if_contains_anagrams(lst):
    count = 0
    for i, word1 in enumerate(lst):
        for j, word2 in enumerate(lst[i + 1:]):
            if len(word1) >= 3 and len(word2) >= 3:
                if sorted(word1.lower()) == sorted(word2.lower()):
                    count += 1
                    if count >= 46:
                        return True
    return count >= 46