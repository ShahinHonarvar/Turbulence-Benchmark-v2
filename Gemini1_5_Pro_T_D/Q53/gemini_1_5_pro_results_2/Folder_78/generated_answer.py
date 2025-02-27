def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 48, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1] and len(substring) >= 96 and substring.isalpha():
                palindromes.add(substring)
    return palindromes