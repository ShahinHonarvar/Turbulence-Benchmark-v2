def if_contains_anagrams(s):
    s = [i.lower() for i in s]
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if len(s[i]) >= 3 and len(s[j]) >= 3 and (sorted(s[i]) == sorted(s[j])):
                return True
    return False