def palindrome_of_length_n(s):
    n = 67
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes