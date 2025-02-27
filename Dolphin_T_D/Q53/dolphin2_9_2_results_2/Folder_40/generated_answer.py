def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    n = 3
    for i in range(len(s)):
        for j in range(i + n - 1, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) >= n:
                palindromes.add(sub)
    return palindromes