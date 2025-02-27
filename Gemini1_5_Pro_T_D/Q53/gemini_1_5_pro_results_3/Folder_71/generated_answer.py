def palindrome_of_length_at_least_n(text):
    text = ''.join((ch for ch in text if ch.isalnum()))
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 87, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes