def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j + 1]
            if len(substring) >= 56 and substring.lower() == substring.lower()[::-1] and all((char.isalpha() for char in substring)):
                palindromes.add(substring)
    return palindromes