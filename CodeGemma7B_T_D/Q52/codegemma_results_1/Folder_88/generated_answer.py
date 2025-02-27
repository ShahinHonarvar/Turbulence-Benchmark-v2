def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1] and len(substring) == 13:
                palindromes.add(substring)
    return palindromes