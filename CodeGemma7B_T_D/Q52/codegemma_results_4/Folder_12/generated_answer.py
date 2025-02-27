def palindrome_of_length_n(text):
    palindromes = set()
    for start in range(len(text)):
        for end in range(start + 23, len(text) + 1):
            substring = text[start:end].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes