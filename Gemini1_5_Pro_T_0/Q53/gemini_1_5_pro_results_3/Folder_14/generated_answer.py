def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 13, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((letter.isalpha() for letter in substring)):
                palindromes.add(substring)
    return palindromes