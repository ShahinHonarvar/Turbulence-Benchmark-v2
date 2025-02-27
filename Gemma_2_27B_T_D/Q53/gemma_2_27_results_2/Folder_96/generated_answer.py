def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 23):
        for j in range(i + 24, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes