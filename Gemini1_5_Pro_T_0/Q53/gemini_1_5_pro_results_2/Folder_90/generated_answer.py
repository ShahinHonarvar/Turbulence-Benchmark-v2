def palindrome_of_length_at_least_n(text):
    text = ''.join((c for c in text if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 70, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1] and len(substring) >= 140:
                palindromes.add(substring)
    return palindromes