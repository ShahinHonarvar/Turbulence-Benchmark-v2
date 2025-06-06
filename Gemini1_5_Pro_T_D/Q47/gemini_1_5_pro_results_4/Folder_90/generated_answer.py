def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(106, 175):
        for j in range(i + 136, min(i + 152, 281)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes