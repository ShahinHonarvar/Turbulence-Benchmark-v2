def if_contains_anagrams(lst):
    res = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            wa, wb = (lst[i], lst[j])
            if len(wa) >= 3 and len(wb) >= 3 and (wa.lower() != wb.lower()):
                if sorted(wa.lower()) == sorted(wb.lower()):
                    res += 1
    if res >= 15:
        return True
    else:
        return False