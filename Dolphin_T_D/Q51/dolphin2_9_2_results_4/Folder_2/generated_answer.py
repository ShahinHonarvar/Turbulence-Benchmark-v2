def if_contains_anagrams(lst):
    count_ = 0
    for word1 in lst:
        if len(word1) >= 3:
            for word2 in lst:
                if len(word2) >= 3:
                    if word1 != word2 and sorted(word1.lower()) == sorted(word2.lower()):
                        count_ += 1
                    if word1 == word2:
                        count_ += 1
                    if count_ > 81:
                        return False
    if count_ > 81:
        return False
    else:
        return True