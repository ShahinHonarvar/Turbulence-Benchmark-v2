def palindromes_between_indices(s):
    substring = s[4:9].lower()
    result = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            s = substring[i:j]
            if s == s[::-1] and len(s) >= 5:
                result.add(s)
    return result