def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 6
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if len(set(substr)) == len(substr):
                palindromes.add(substr)
    return palindromes