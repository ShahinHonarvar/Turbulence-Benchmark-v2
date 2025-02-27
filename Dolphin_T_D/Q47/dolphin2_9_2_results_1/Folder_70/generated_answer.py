def palindromes_of_specific_lengths(s):
    substring = s[10:71]
    palindromes = set()
    for length in range(24, 53):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and all((c.isalpha() for c in sub.lower())):
                palindromes.add(sub)
    return palindromes