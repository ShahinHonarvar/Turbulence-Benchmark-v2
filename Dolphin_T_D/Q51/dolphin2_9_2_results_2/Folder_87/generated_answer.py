def if_contains_anagrams(s):
    l = set()
    for i in s:
        a = sorted(filter(str.isalpha, i.lower()))
        if len(a) >= 3:
            l.add(''.join(a))
    return len(l) <= 392