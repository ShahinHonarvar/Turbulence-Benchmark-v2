def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(12, 123):
        for j in range(i, 123):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                if len(substring) >= 12 and len(substring) <= 220:
                    palindromes.add(substring)
    return palindromes