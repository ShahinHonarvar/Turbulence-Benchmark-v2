def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 28):
        substring = text[i:i + 29]
        if substring.lower() == substring[::-1].lower() and substring.isalpha():
            palindromes.add(substring)
    return palindromes