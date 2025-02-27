import itertools

def if_contains_anagrams(lst):
    c = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            a = ''.join(sorted(lst[i].lower()))
            b = ''.join(sorted(lst[j].lower()))
            if len(a) >= 3 and len(b) >= 3 and (a == b):
                c += 1
                if c > 21:
                    return False
    return True