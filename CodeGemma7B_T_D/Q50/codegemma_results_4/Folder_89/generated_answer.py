def if_contains_anagrams(str_list):
    str_list.sort(key=len)
    in_degree = {}
    out_degree = {}
    for str in str_list:
        if len(str) < 3:
            continue
        str_sorted = sorted(str.lower())
        str_key = ''.join(str_sorted)
        if str_key in in_degree:
            in_degree[str_key] += 1
            if in_degree[str_key] >= 36:
                return True
        else:
            in_degree[str_key] = 1
            out_degree[str_key] = 0
    for str in str_list:
        str_sorted = sorted(str.lower())
        str_key = ''.join(str_sorted)
        out_degree[str_key] += 1
        if out_degree[str_key] >= 36:
            return True
    return False