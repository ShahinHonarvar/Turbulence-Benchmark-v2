def palindrome_of_length_at_least_n(text):
    palindromes = set()
    text = text.lower()
    text = ''.join((t for t in text if t.isalpha()))
    text = text.replace(' ', '')
    for i in range(len(text)):
        for j in range(i + 76, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes