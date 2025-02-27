def palindromes_between_indices(text):
    letters = ''.join((chr for chr in text[:4].lower() if chr.isalpha()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = letters[i:j + 1]
            if len(substring) >= 4 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes