def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(0, len(text) - 41):
        for j in range(i + 42, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes