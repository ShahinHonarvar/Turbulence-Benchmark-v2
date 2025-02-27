def palindrome_of_length_at_least_n(text):
    palindromes = set()
    text = text.lower()
    for i in range(len(text) - 37):
        for j in range(i + 38, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes