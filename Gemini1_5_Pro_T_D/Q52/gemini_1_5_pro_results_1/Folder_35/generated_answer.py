def palindrome_of_length_n(text):
    palindromes = set()
    text = text.lower()
    for i in range(len(text) - 115):
        substring = text[i:i + 116]
        if substring == substring[::-1]:
            if substring.isalpha():
                palindromes.add(substring)
    return palindromes