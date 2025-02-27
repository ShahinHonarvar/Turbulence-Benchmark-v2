def palindrome_of_length_n(s):
    s = s.lower()
    n = 401
    palindromes = set()
    for i in range(n, len(s) + 1):
        for j in range(i - n, i):
            sub = s[j:i]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes