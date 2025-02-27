def palindromes_of_specific_lengths(text):
    text = text[31:92].lower()
    palindromes = set()
    for i in range(len(text) - 50 + 1):
        for length in range(50, 54):
            if i + length <= len(text):
                substring = text[i:i + length]
                if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes