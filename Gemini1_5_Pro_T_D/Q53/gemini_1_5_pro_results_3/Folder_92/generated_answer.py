def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 9):
        for j in range(i + 10, len(text) + 1):
            substring = text[i:j]
            if ''.join((c for c in substring.lower() if c.isalpha())) == ''.join((c for c in reversed(substring.lower()) if c.isalpha())):
                palindromes.add(substring)
    return palindromes