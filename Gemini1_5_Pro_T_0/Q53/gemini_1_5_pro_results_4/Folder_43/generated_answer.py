def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 48):
        for j in range(i + 49, len(text) + 1):
            substring = text[i:j]
            if len(substring) >= 49 and substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes