def palindromes_of_specific_lengths(s):
    s = s[70:141].lower()
    palindromes_set = set()
    n = len(s)
    for start in range(n):
        for end in range(start + 2, min(n, start + 60) + 1):
            substring = s[start:end + 1]
            if all((c.isalpha() for c in substring)) and substring == substring[::-1]:
                palindromes_set.add(substring)
    return palindromes_set