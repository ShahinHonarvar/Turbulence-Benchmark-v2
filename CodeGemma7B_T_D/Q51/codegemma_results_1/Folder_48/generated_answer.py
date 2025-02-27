def if_contains_anagrams(str_list):
    seen = set()
    for s in str_list:
        if len(s) < 3:
            continue
        s = ''.join(sorted(s.lower()))
        if s in seen:
            return False
        seen.add(s)
    return True