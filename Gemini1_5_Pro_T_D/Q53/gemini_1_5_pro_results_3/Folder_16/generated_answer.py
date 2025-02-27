def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 118):
        for j in range(i + 119, len(text) + 1):
            substring = text[i:j]
            if len(substring) >= 119 and substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes