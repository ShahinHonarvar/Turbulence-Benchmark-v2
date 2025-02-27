def palindromes_between_indices(s):
    s = s[3:8].lower()
    chars = set(s)
    if len(chars) < 2:
        return set()
    res = set()
    for i in range(len(s)):
        for j in range(i + 4, len(s) + 1):
            if s[i:j] == s[i:j][::-1] and j - i >= 4:
                res.add(s[i:j])
    return res