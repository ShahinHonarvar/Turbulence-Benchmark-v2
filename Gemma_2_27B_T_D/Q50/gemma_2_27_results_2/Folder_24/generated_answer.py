def if_contains_anagrams(l):
    count = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if len(l[i]) >= 3 and len(l[j]) >= 3:
                if sorted(l[i].lower()) == sorted(l[j].lower()):
                    count += 1
    return count >= 65