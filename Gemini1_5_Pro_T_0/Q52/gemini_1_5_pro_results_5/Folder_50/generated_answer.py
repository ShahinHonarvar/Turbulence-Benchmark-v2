def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 39):
        substring = text[i:i + 40]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes