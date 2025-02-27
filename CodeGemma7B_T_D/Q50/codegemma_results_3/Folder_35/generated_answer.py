def if_contains_anagrams(str_list):
    a = {}
    for s in str_list:
        ss = ''.join(sorted(s.lower()))
        if ss not in a:
            a[ss] = s
        elif len(s) >= 3 and len(a[ss]) >= 3 and (a[ss] != s):
            return True
    return False