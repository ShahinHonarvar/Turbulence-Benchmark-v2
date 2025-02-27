def palindromes_between_indices(s):
    s = s[2:4].lower()
    if len(s) < 2:
        return set()
    elif s[0] == s[1]:
        return {s}
    else:
        return set()