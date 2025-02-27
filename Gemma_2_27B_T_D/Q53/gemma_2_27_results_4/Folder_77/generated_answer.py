def palindrome_of_length_at_least_n(text):
    palindromes = set()
    text = text.lower()
    for i in range(len(text) - 148):
        for j in range(i + 148, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1] and len(substring) >= 149:
                palindromes.add(substring)
    return palindromes