def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 63):
        sub = s[i:i + 64]
        if sub == sub[::-1] and all((char.isalpha() for char in sub)):
            palindromes.add(sub)
    return palindromes