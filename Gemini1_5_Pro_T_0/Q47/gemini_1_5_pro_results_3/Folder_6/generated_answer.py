def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(45, 98 - 39):
        for j in range(40, 48):
            substring = text[i:i + j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:i + j])
    return palindromes