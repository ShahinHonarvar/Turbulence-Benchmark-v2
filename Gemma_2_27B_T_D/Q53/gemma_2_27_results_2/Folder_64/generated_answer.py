def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 8):
        substring = text[i:i + 9].lower()
        if substring == substring[::-1]:
            palindromes.add(text[i:i + 9])
    for i in range(len(text) - 9):
        substring = text[i:i + 10].lower()
        if substring == substring[::-1]:
            palindromes.add(text[i:i + 10])
    return palindromes