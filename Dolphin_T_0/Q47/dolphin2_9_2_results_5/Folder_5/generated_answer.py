def palindromes_of_specific_lengths(s):
    substring = s[63:71]
    palindromes = set()
    for i in range(4, 6):
        for j in range(0, len(substring) - i + 1):
            sub = substring[j:i + j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes