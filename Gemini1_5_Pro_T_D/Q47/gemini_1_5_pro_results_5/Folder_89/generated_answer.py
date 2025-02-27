def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 89):
        for j in range(i + 1, min(89, i + 14)):
            substring = text[i:j].lower()
            if 12 <= len(substring) <= 14 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(text[i:j])
    return palindromes