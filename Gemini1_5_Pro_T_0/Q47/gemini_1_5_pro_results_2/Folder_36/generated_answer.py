def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(124, 284):
        for j in range(i + 115, min(i + 135, 284)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes