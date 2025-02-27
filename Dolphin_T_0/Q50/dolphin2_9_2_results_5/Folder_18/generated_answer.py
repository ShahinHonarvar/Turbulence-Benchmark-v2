def if_contains_anagrams(s):
    c = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if len(s[i]) >= 3 and len(s[j]) >= 3 and (sorted(s[i].lower()) == sorted(s[j].lower())):
                c += 1
                if c >= 106:
                    return True
    return False