def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 35):
        for j in range(i + 36, len(text) + 1):
            substring = text[i:j]
            if len(substring) >= 36 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes