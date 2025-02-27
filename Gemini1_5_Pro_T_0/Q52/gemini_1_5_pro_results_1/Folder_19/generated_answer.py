def palindrome_of_length_n(text):
    text = text.lower()
    n = 67
    palindromes = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes