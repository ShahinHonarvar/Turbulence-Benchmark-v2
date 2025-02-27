def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(39, 95):
        for j in range(i + 14, i + 53):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes