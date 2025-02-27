def if_contains_anagrams(ls):
    result = False
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            if len(ls[i]) >= 3 and len(ls[j]) >= 3:
                if sorted(ls[i].lower()) == sorted(ls[j].lower()):
                    result = True
    return result