def palindrome_of_length_n(s):
    s = s.upper()
    palindromes = set()
    for i in range(len(s) - 46):
        sub = s[i:i + 47]
        if sub == sub[::-1] and all((c.isalpha() for c in sub)):
            palindromes.add(sub)
    return palindromes