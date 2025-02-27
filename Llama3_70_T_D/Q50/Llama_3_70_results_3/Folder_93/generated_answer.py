def if_contains_anagrams(lst):
    lst = [x.lower() for x in lst if len(x) >= 3]
    d = {}
    for s in lst:
        sorted_str = ''.join(sorted(s))
        if sorted_str in d:
            d[sorted_str] += 1
        else:
            d[sorted_str] = 1
    count = 0
    for v in d.values():
        count += sum(range(1, v))
    return count >= 18