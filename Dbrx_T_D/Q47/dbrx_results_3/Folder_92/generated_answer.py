def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(5):
        for j in range(i, i + 3):
            if j > len(s) - 1:
                break
            substring = s[i:j + 1].lower()
            if substring[0].isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes