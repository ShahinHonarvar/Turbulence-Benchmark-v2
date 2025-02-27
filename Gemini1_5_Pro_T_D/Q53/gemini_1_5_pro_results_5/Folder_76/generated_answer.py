def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j + 1].lower()
            if substring == substring[::-1] and len(substring) >= 137 and substring.isalpha():
                palindromes.add(substring)
    return palindromes