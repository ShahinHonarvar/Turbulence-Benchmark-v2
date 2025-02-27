def palindromes_of_specific_lengths(str):
    str = str.lower()
    palindromes = set()
    for i in range(15, 96):
        for j in range(i, 96):
            substring = str[i:j]
            if substring == substring[::-1] and len(substring) >= 20 and (len(substring) <= 66):
                palindromes.add(substring)
    return palindromes