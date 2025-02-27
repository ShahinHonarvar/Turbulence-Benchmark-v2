def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(21, 62 - 21):
        for j in range(i + 22, min(i + 34, 63)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes