def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = []
    for i in range(len(text) - 71):
        for j in range(i + 1, len(text) - 70):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindromes.append(substring)
    return set(palindromes)