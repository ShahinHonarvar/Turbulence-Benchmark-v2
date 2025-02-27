def if_contains_anagrams(lst):
    count = 0
    for word1 in lst:
        if len(word1) >= 3:
            for word2 in lst:
                if word1 != word2 and len(word2) >= 3:
                    sorted_word1 = ''.join(sorted(word1.lower()))
                    sorted_word2 = ''.join(sorted(word2.lower()))
                    if sorted_word1 == sorted_word2:
                        count += 1
                        if count >= 81:
                            return True
    return False