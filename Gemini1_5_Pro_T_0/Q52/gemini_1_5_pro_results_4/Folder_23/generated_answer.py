def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 68):
        substring = text[i:i + 69].lower()
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes