def if_contains_anagrams(list_of_strings):
    agg = {}
    for string in list_of_strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            if key in agg:
                agg[key] += 1
            else:
                agg[key] = 1
    length = 0
    for k in agg.values():
        length += k * (k - 1) // 2
    return length >= 40