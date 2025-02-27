def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(51):
        for j in range(i, min(len(text), 51)):
            substring = text[i:j + 1].lower()
            if 50 <= len(substring) <= 100 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes