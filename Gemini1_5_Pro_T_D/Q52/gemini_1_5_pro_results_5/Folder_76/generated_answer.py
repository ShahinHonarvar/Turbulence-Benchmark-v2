def palindrome_of_length_n(text):
    palindromes = set()
    n = 257
    for i in range(len(text) - n + 1):
        substring = text[i:i + n].lower()
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes