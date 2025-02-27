def if_contains_anagrams(s):
    res = []
    for p in range(len(s)):
        for q in range(p + 1, len(s)):
            if len(s[p]) >= 3 and len(s[q]) >= 3 and (sorted(s[p].lower()) == sorted(s[q].lower())):
                res.append([s[p], s[q]])
                if len(res) == 10:
                    return True
    if len(res) <= 9:
        return False
    else:
        return True