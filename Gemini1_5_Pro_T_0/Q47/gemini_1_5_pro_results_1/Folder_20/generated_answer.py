def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(20, 55):
        for j in range(i + 36, i + 43):
            if j > 74:
                break
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes