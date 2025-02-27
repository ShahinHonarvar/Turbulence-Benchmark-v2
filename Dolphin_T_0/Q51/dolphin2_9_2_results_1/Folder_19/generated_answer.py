from collections import Counter

def if_contains_anagrams(l):
    counts_l = [Counter(i.lower()) for i in l]
    pairs = 0
    for i in range(len(counts_l)):
        for j in range(i + 1, len(counts_l)):
            if len(counts_l[i]) >= 3 and len(counts_l[j]) >= 3 and (counts_l[i] == counts_l[j]):
                pairs += 1
                if pairs >= 69:
                    return True
    return False