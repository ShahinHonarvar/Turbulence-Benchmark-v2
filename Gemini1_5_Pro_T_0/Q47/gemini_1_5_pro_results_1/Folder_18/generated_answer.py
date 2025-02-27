def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 83):
        for j in range(i, 84):
            substring = text[i:j + 1]
            if 13 <= len(substring) <= 66 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes