def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 18):
        for j in range(19, len(text) - i + 1):
            substring = text[i:i + j]
            if substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes