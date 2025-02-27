def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 40):
        for j in range(i + 41, len(text) + 1):
            substring = text[i:j]
            if len(substring) >= 41 and all((c.isalpha() for c in substring)):
                if substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes