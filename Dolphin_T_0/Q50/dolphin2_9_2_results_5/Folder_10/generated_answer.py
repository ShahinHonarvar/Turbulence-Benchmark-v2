import collections

def if_contains_anagrams(lst):
    count = 0
    for word1 in lst:
        if len(word1) >= 3:
            for word2 in lst:
                if len(word2) >= 3 and word1 != word2:
                    sorted1 = ''.join(sorted(word1.lower()))
                    sorted2 = ''.join(sorted(word2.lower()))
                    if sorted1 == sorted2:
                        count += 1
                        lst.remove(word2)
                        break
    return count >= 52