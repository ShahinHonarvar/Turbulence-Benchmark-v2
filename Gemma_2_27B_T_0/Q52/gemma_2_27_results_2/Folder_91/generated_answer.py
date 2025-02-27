def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 6):
        substring = text[i:i + 7].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes