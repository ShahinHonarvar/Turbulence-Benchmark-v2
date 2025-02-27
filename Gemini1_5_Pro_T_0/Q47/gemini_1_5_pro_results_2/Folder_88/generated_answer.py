def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 87 - 3):
        for j in range(i + 3, min(i + 6, 88)):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring.lower())
    return palindromes