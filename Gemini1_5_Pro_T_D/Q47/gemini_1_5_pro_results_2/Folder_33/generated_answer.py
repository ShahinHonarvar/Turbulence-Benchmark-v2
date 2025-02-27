def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(130, 295):
        for j in range(i + 103, min(i + 159, 296)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes