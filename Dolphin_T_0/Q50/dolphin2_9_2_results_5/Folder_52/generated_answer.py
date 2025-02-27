def if_contains_anagrams(l):
    count = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if len(l[i]) < 3 or len(l[j]) < 3:
                continue
            l[i] = l[i].lower()
            l[j] = l[j].lower()
            if sorted(l[i]) == sorted(l[j]):
                count += 1
    return count >= 58