def if_contains_anagrams(str_list):
    str_list = [i.lower() for i in str_list]
    seen = set()
    pairs = set()
    for i in sorted(str_list):
        for j in str_list:
            if i != j and len(i) >= 3 and (len(j) >= 3):
                key = tuple(sorted(i))
                if key in seen:
                    pairs.add((seen[key], i))
                    if len(pairs) >= 57:
                        return True
                seen[key] = i
                key = tuple(sorted(j))
                if key in seen:
                    pairs.add((seen[key], j))
                    if len(pairs) >= 57:
                        return True
                seen[key] = j
    return len(pairs) >= 57