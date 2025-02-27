def palindrome_of_length_at_least_n(text):
    text = text.lower()
    text_len = len(text)
    palindromes = set()
    for i in range(text_len):
        for j in range(i, text_len):
            substring = text[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes