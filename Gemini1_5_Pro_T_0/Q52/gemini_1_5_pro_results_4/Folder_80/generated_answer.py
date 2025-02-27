def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 275):
        substring = text[i:i + 276]
        if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes