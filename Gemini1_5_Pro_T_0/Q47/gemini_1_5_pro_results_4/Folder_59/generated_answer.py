def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(101):
        for j in range(i + 1, min(101, i + 15)):
            substring = text[i:j].lower()
            if 3 <= len(substring) <= 15 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes