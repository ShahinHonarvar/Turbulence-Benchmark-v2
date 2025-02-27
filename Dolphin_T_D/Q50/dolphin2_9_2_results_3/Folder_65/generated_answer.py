def if_contains_anagrams(lst):
    count = 0
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            for sc in lst:
                if len(sc) >= 3 and sc != s and (''.join(sorted(sc.lower())) == sorted_s):
                    count += 1
                    if count >= 94:
                        return True
    return False