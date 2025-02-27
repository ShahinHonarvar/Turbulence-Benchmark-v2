def palindromes_between_indices(s):
    s = s[:5].lower()
    result = set()
    for a in range(len(s)):
        for b in range(a + 1, len(s) + 1):
            sub = s[a:b]
            if len(sub) >= 4 and sub == sub[::-1]:
                result.add(sub)
    return result