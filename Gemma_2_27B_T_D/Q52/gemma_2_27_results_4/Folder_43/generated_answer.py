def palindrome_of_length_n(text):
    palindromes = set()
    text = text.lower()
    for i in range(len(text) - 50):
        substring = text[i:i + 51]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes