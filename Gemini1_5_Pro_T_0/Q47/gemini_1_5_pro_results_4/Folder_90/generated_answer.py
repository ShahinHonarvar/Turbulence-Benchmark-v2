def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(106, 281):
        for j in range(i + 135, min(i + 151, 281) + 1):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes