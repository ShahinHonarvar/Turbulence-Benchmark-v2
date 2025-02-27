def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11):
        for j in range(i + 1, min(len(text), 11)):
            substring = text[i:j + 1]
            if 3 <= len(substring) <= 5 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes