def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 61):
        for j in range(i + 62, len(text) + 1):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes