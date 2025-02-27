def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 63):
        substring = s[i:i + 64].lower()
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes