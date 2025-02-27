def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for length in range(68, len(text) + 1):
        for i in range(len(text) - length + 1):
            substring = text[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes