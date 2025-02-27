def if_contains_anagrams(str_list):
    dict = {}
    for str in str_list:
        tmp = ''.join(sorted(str.lower()))
        if len(tmp) < 3:
            continue
        if tmp in dict:
            dict[tmp] += 1
            if dict[tmp] > 9:
                return False
        else:
            dict[tmp] = 1
    return True