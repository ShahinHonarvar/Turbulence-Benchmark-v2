def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(62, 88 - 17):
        for j in range(i + 18, min(i + 22, 89)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes