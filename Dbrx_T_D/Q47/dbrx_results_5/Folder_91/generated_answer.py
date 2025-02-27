def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for length in range(3, 6):
        for index in range(0, 11 - length + 1):
            substring = s[index:index + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes