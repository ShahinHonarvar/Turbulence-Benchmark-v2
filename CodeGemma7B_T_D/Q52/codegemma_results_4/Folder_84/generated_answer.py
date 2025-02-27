def palindrome_of_length_n(text):
    if len(text) < 131:
        return set()
    palindromes = set()
    for i in range(len(text) - 130 + 1):
        for j in range(i + 130):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes