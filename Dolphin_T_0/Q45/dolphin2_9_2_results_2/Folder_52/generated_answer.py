def palindromes_between_indices(s):
    a = set()
    for i in range(6, min(8, len(s)) + 1):
        for j in range(len(s)):
            p = s[j:j + i]
            p_rev = p[::-1]
            if p != p_rev and p == p_rev.lower():
                a.add(p)
    return a