from collections import Counter

def if_contains_anagrams(l):
    count = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            w1 = l[i].lower()
            w2 = l[j].lower()
            if len(w1) >= 3 and len(w2) >= 3 and (Counter(w1) == Counter(w2)):
                count += 1
    return count <= 58