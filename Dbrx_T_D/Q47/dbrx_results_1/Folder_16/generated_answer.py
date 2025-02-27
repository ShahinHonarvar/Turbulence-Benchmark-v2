def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(15, 87):
        for j in range(i - 49, i - 60, -1):
            substring = s[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes