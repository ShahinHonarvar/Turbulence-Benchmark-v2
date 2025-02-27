def palindrome_of_length_at_least_n(text):
    if not text or len(text) < 29:
        return set()
    text = ''.join((char.lower() for char in text if char.isalpha()))
    palindromes = set()
    for i in range(len(text) - 28):
        substring = text[i:i + 29]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes