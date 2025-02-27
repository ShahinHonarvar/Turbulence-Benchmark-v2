def palindrome_of_length_n(text):
    palindromes = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1] and len(substring) == 423:
                palindromes.add(substring)
    return palindromes