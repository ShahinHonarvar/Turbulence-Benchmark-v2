from collections import Counter

def if_contains_anagrams(l):
    count = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if len(l[i]) >= 3 and len(l[j]) >= 3 and (Counter(l[i].lower()) == Counter(l[j].lower())):
                count += 1
    return count >= 153