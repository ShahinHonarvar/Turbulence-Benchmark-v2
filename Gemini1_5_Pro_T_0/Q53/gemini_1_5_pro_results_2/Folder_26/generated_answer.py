def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 31):
        for j in range(i + 32, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes