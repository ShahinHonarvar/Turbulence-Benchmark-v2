def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 146):
        substring = text[i:i + 147].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes