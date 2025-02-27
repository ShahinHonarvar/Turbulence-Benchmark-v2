def palindromes_between_indices(s):
    result = set()
    for i in range(len(s) - 6):
        for j in range(i + 1, len(s) - 5):
            for k in range(j + 1, len(s) - 4):
                for l in range(k + 1, len(s) - 3):
                    for m in range(l + 1, len(s) - 2):
                        for n in range(m + 1, len(s) - 1):
                            for o in range(n + 1, len(s)):
                                if s[i].lower() == s[o].lower() and s[j].lower() == s[n].lower() and (s[k].lower() == s[m].lower()) and (s[l].lower() == s[o].lower()):
                                    if i + 7 == o and j + 6 == n and (k + 5 == m) and (l + 4 == o):
                                        result.add(s[i:o + 1])
    return result