def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 99):
        substring = text[i:i + 100].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes