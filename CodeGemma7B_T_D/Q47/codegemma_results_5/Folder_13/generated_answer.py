def palindromes_of_specific_lengths(str):
    seen = set()
    for i in range(13, 96):
        for j in range(i, 95):
            s = str[i:j + 1]
            if s == s[::-1] and 57 <= len(s) <= 60 and s.isalpha():
                seen.add(s)
    if not seen:
        return set()
    return seen