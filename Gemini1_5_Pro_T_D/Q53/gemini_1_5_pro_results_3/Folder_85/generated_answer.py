def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 85, len(text) + 1):
            substring = text[i:j]
            if len(substring) >= 85 and substring.lower() == substring.lower()[::-1] and all((letter.isalpha() for letter in substring)):
                palindromes.add(substring)
    return palindromes