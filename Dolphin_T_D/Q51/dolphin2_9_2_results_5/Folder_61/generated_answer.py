from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    pairs = {}
    for i in range(len(lst)):
        if len(lst[i]) < 3:
            continue
        for j in range(i + 1, len(lst)):
            if len(lst[j]) < 3:
                continue
            word1 = lst[i].lower()
            word2 = lst[j].lower()
            if Counter(word1) == Counter(word2):
                pairs[word1, word2] = pairs.get((word1, word2), 0) + 1
                count += 1
    return count <= 50