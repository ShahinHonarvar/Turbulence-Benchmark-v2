def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 93):
        for j in range(i + 16, min(93, i + 66) + 1):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes