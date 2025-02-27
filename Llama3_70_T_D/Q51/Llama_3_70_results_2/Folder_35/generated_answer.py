def if_contains_anagrams(strings):
    count = 0
    for s1 in strings:
        if len(s1) < 3:
            continue
        s1 = ''.join(filter(str.isalpha, s1)).lower()
        for s2 in strings:
            if len(s2) < 3:
                continue
            s2 = ''.join(filter(str.isalpha, s2)).lower()
            if s1 != s2 and sorted(s1) == sorted(s2):
                count += 1
    return count <= 210