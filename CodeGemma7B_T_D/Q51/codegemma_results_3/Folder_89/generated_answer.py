def if_contains_anagrams(str_list):
    str_list = sorted(str_list, key=len)
    lookup = {}
    results = 0
    for str in str_list:
        if str in lookup:
            results += 1
            if results >= 73:
                return False
        else:
            sorted_str = ''.join(sorted(str.lower()))
            if sorted_str in lookup:
                lookup[sorted_str] += 1
            else:
                lookup[sorted_str] = 1
    return True