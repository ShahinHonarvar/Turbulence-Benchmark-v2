def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 2):
        for j in range(i + 3, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes