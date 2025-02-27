def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 2):
        substring = text[i:i + 3]
        if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
            palindromes.add(substring.lower())
    return palindromes