def if_contains_anagrams(str_list):
    str_set = set()
    count = 0
    for s in str_list:
        if len(s) < 3:
            continue
        s = ''.join(sorted(s.lower()))
        if s in str_set:
            count += 1
            if count > 34:
                return False
        else:
            str_set.add(s)
    return True