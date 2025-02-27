def palindromes_of_specific_lengths(s):
    substring = s[101:293]
    palindromes = set()
    for length in range(154, 183):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes