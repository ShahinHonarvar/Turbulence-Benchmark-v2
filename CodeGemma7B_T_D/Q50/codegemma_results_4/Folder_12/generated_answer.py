def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list.sort()
    str_set = set()
    num_pairs = 0
    for s in str_list:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in str_set:
            num_pairs += 1
        else:
            str_set.add(sorted_s)
            num_pairs = 0
        if num_pairs >= 69:
            return True
    return False