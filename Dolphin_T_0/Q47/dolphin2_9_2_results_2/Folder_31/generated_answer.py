def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[11:84]
    for length in range(37, 61):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length].lower():
                palindromes.add(substring[i:i + length])
    return palindromes