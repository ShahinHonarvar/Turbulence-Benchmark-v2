def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 301):
        for j in range(50, 101):
            if i + j <= len(text) + 1:
                substring = text[i:i + j].lower()
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(text[i:i + j])
    return palindromes