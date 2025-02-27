def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 55):
        for j in range(i + 56, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes