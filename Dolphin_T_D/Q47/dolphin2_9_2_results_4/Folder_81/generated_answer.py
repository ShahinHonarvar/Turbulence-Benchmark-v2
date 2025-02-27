def palindromes_of_specific_lengths(s):
    substring = s[12:122]
    palindromes = set()
    for length in range(12, 221):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length].lower()
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes