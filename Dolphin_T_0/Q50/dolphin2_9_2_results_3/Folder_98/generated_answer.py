def if_contains_anagrams(l):
    count = 0
    for i in l:
        if len(i) >= 3:
            for j in l:
                if sorted(i.lower()) == sorted(j.lower()) and i != j:
                    count += 1
    if count >= 14:
        return True
    else:
        return False