def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 90):
        for j in range(i + 90, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes