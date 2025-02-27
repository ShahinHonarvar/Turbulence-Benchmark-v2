def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 136):
        for j in range(i + 137, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring[::-1].lower() and ''.join((c for c in substring if c.isalpha())).lower() == substring.lower():
                palindromes.add(substring)
    return palindromes