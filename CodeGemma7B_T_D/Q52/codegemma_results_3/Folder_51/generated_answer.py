def palindrome_of_length_n(text):
    text_lower = text.lower()
    palindromes = set()
    for i in range(len(text_lower)):
        for j in range(i + 73, len(text_lower)):
            substring = text_lower[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes