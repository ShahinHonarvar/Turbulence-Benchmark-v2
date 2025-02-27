def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 301):
        for j in range(50, 101):
            if i + j <= len(text) + 1:
                substring = text[i:i + j]
                if len(substring) >= 50 and len(substring) <= 100 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                    palindromes.add(substring)
    return palindromes