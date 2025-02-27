def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(21, 62 - 21 + 1):
        for j in range(i + 22, min(i + 33, 62) + 1):
            substring = text[i:j + 1]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes