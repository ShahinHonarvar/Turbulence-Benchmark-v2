from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            word1 = lst[i].lower()
            word2 = lst[j].lower()
            if len(word1) >= 3 and len(word2) >= 3 and (Counter(word1) == Counter(word2)):
                pairs.append((i, j))
                count += 1
                if count == 17:
                    return True
    if count <= 17:
        return True
    else:
        return False