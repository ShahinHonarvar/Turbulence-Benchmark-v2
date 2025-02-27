def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 210 + 1):
        substring = text[i:i + 210].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes