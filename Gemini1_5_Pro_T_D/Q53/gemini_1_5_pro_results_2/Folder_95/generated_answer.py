def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(0, len(text) - 34):
        for j in range(i + 35, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes