def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 66):
        substring = text[i:i + 67].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes