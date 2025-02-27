def palindromes_between_indices(s):
    s = s[8:10].lower()
    return {a + b + a for a in s for b in s if a == a[::-1] and b == b[::-1] and (len(a + b + a) >= 3)}