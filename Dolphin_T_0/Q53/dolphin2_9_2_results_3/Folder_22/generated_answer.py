def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 96):
        for j in s[i:]:
            if j == j[::-1] and len(j) >= 97:
                palindromes.add(j)
    return palindromes