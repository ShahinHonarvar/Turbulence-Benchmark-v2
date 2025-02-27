def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(27, 96):
        for j in range(i + 49, i + 52):
            if j <= 95:
                substring = text[i:j].lower()
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(text[i:j])
    return palindromes