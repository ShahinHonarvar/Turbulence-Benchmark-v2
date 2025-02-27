def palindrome_of_length_at_least_n(text):
    palindromes = set()
    text = text.lower()
    n = len(text)
    for i in range(n):
        for j in range(i + 73, n + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes