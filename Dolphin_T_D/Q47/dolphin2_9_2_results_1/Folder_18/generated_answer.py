def palindromes_of_specific_lengths(s):
    substring = s[11:84]
    palindromes = set()
    for i in range(13, 67):
        for j in range(len(substring) - i + 1):
            if substring[j:j + i].lower() == substring[j:j + i].lower()[::-1] and substring[j:j + i].isalpha():
                palindromes.add(substring[j:j + i])
    return palindromes