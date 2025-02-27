def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11):
        for j in range(i + 1, min(len(text), i + 5)):
            substring = text[i:j].lower()
            if 3 <= len(substring) <= 5 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes