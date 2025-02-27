def palindrome_of_length_at_least_n(text):
    text = ''.join((c for c in text if c.isalpha())).lower()
    palindromes = set()
    for i in range(0, len(text) - 79):
        for j in range(i + 80, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes