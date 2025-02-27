from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                word1, word2 = (lst[i].lower(), lst[j].lower())
                counter1, counter2 = (Counter(word1), Counter(word2))
                if counter1 == counter2:
                    pairs += 1
                    if pairs > 98:
                        return False
    return pairs <= 98