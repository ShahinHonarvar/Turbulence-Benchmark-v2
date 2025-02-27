def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(127, 289):
        for j in range(i, 289):
            substring = text[i:j + 1]
            if len(substring) >= 119 and len(substring) <= 141 and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes