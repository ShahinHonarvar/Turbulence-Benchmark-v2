def palindrome_of_length_at_least_n(text):
    palindromes = set()
    text_lower = text.lower()
    for start in range(len(text_lower)):
        for end in range(len(text_lower), start, -1):
            substring = text_lower[start:end + 1]
            if substring == substring[::-1] and len(substring) >= 67:
                palindromes.add(substring)
    return palindromes