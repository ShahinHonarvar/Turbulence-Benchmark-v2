def palindrome_of_length_n(text):
    text = ''.join((c for c in text if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(text) - 256):
        substring = text[i:i + 257]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes