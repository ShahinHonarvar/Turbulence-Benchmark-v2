def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 84):
        for j in range(85, len(text) - i + 1):
            substring = text[i:i + j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes