def if_contains_anagrams(str_list):
    seen = set()
    for str in str_list:
        key = tuple(sorted(str.lower()))
        if key in seen:
            return True
        seen.add(key)
    return False