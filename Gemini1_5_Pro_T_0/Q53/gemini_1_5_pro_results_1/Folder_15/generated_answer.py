def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(0, len(text) - 3):
        for j in range(i + 3, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes