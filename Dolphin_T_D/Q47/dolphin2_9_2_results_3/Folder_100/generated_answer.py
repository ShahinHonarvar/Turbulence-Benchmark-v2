def palindromes_of_specific_lengths(s):
    substring = s[29:97]
    palindromes = set()
    for length in range(12, 19):
        for index in range(len(substring) - length + 1):
            if all((c.isalpha() for c in substring[index:index + length])) and substring[index:index + length] == substring[index:index + length][::-1]:
                palindromes.add(substring[index:index + length].lower())
    return palindromes