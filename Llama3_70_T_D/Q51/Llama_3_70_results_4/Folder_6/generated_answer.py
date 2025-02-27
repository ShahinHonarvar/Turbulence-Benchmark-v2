def if_contains_anagrams(lst):
    seen = {}
    count = 0
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in seen:
            count += seen[sorted_s]
            if count > 86:
                return False
            seen[sorted_s] += 1
        else:
            seen[sorted_s] = 1
    return True