def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 56):
        substring = text[i:i + 57].lower()
        if substring == substring[::-1]:
            palindromes.add(text[i:i + 57])
    return palindromes