def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 78):
        for j in range(i + 43, i + 48):
            if j <= 78:
                substring = text[i:j].lower()
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(text[i:j])
    return palindromes