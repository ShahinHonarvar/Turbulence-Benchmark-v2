def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 317):
        substring = text[i:i + 318]
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes