def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 148):
        for j in range(i + 149, len(text) + 1):
            substring = text[i:j]
            if ''.join((c for c in substring if c.isalpha())).lower() == ''.join((c for c in substring if c.isalpha()))[::-1].lower():
                palindromes.add(substring)
    return palindromes