def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 75):
        substring = text[i:i + 76].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes