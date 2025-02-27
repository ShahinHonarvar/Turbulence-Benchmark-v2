def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 222):
        substring = text[i:i + 223].lower()
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes