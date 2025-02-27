def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 73):
        for j in range(i, 73):
            substring = text[i:j + 1]
            if len(substring) >= 19 and len(substring) <= 55:
                if substring.lower() == substring[::-1].lower() and all((char.isalpha() for char in substring)):
                    palindromes.add(substring)
    return palindromes