def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for start in range(len(text)):
        for end in range(start + 141, len(text) + 1):
            substring = text[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes