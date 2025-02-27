def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 38):
        substring = text[i:i + 39]
        if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes