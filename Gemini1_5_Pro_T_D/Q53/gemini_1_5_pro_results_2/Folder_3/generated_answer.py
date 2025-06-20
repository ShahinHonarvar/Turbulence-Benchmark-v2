def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 59, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes