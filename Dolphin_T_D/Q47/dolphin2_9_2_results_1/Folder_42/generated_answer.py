def palindromes_of_specific_lengths(s):
    substring = s[43:96]
    palindromes = set()
    for length in range(18, 48):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes