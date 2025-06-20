def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 146):
        for j in range(i + 147, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(text[i:j])
    return palindromes