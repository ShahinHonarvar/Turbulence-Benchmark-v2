def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 83):
        for j in range(i + 84, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes