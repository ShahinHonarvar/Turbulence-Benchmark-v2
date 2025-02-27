def if_contains_anagrams(str_list):
    count = 0
    for word1 in str_list:
        if len(word1) >= 3:
            for word2 in str_list:
                if len(word2) >= 3 and word1 != word2 and (sorted(word1.lower()) == sorted(word2.lower())):
                    count += 1
                    if count > 69:
                        return False
    return True