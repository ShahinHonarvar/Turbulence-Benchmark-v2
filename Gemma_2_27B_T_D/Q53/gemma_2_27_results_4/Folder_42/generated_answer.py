def palindrome_of_length_at_least_n(text):
    palindromes = set()
    text = text.lower()
    for i in range(len(text) - 43):
        for j in range(i + 44, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes