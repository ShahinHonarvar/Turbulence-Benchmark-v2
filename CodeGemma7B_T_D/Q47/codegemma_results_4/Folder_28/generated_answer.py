def palindromes_of_specific_lengths(txt):
    palindromes = set()
    txt = txt.lower()
    for i in range(32, 72):
        for j in range(i, 72):
            substring = txt[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes