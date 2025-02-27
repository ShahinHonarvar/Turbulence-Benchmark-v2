def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 91):
        for j in range(i + 92, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes