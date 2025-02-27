def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 36
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n - 1, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes