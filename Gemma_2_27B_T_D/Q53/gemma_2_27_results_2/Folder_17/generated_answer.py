def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 35):
        for j in range(i + 35, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring[::-1].lower() and len(substring) >= 36:
                palindromes.add(substring)
    return palindromes