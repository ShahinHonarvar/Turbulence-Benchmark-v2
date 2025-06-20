def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 53):
        substring = text[i:i + 54].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes