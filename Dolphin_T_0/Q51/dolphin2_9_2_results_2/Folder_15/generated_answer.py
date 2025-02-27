from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for _ in range(len(lst)):
        word1 = lst[_]
        for __ in range(len(lst)):
            if __ == _:
                continue
            word2 = lst[__]
            counter1 = Counter(word1.lower())
            counter2 = Counter(word2.lower())
            if len(word1) >= 3 and len(word2) >= 3 and (counter1 == counter2):
                count += 1
                break
        if count > 20:
            return False
    return count > 0