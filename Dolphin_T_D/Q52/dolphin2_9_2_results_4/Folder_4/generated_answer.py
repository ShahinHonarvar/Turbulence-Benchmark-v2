def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 14, n):
            sub = s[i:j + 1]
            if sub == sub[::-1] and len(sub) <= 15:
                palindromes.add(sub)
    return palindromes