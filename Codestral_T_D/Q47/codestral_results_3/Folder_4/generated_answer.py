def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(17, 67):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring[12:93].isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes