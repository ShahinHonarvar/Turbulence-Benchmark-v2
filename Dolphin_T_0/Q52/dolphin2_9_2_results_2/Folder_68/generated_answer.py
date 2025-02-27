def palindrome_of_length_n(s):
    s = s.lower()
    n = 76
    palindromes = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if all((c.isalpha() for c in sub)) and sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes