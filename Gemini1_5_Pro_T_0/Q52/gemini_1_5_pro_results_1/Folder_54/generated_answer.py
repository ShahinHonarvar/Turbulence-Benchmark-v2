def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 84):
        substring = text[i:i + 85]
        if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes