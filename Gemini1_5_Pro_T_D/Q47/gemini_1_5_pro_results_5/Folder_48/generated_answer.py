def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(155, 284):
        for j in range(i + 104, min(i + 121, 284)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes