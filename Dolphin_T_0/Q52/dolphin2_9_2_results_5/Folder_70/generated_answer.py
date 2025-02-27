def palindrome_of_length_n(s):
    s = s.lower()
    n = 401
    palindromes = set()
    for i in range(len(s) - n + 1):
        sub = s[i:n + i]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes