def if_contains_anagrams(L):
    count = 0
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if len(L[i]) >= 3 and len(L[j]) >= 3 and (sorted(L[i].lower()) == sorted(L[j].lower())):
                count += 1
    return count >= 48