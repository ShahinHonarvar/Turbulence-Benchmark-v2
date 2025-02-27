from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                word1 = ''.join(sorted(lst[i].lower()))
                word2 = ''.join(sorted(lst[j].lower()))
                if Counter(word1) == Counter(word2):
                    pairs += 1
    return pairs >= 246