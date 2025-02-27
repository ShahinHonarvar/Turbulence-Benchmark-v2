def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 51):
        for j in range(3, 8):
            if i + j <= 56:
                substring = text[i:i + j]
                if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring.lower())
    return palindromes