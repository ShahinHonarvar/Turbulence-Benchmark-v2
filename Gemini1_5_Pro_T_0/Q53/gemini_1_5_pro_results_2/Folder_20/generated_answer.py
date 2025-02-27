def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 5):
        for j in range(i + 6, len(text) + 1):
            substring = text[i:j]
            if len(substring) >= 66 and substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes