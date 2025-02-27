def if_contains_anagrams(l):
    a = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if sorted(l[i].lower()) == sorted(l[j].lower()) and len(l[i]) >= 3 and (len(l[j]) >= 3):
                a += 1
                if a >= 67:
                    return False
    return True