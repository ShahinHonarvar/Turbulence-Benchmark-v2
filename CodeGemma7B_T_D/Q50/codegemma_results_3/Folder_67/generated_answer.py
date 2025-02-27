def if_contains_anagrams(str_list):
    str_lower = [s.lower() for s in str_list]
    str_sort = sorted(str_lower, key=len)
    pairs = []
    for i in range(len(str_sort)):
        for j in range(i + 1, len(str_sort)):
            if sorted(str_sort[i]) == sorted(str_sort[j]) and len(str_sort[i]) >= 3:
                pairs.append((str_sort[i], str_sort[j]))
    return len(pairs) >= 41