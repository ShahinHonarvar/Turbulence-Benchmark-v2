def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 122, len(text) + 1):
            substring = text[i:j]
            if len(substring) >= 122 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes