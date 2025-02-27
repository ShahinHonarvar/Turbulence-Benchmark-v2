def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(45, 52):
        for j in range(40, 95 - i + 40):
            substring = s[j:j + i]
            if substring == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes