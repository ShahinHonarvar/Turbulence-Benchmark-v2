def palindrome_of_length_at_least_n(text):
    text = ''.join((c for c in text if c.isalpha()))
    palindromes = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j + 1]
            if len(substring) >= 150 and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes