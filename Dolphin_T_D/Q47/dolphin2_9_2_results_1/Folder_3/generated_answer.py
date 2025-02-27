def palindromes_of_specific_lengths(s):
    substring = s[27:96]
    palindromes = set()
    for i in range(49, 52):
        for j in range(len(substring) - i + 1):
            subarr = substring[j:j + i]
            if all((c.isalpha() for c in subarr)) and subarr.lower() == subarr[::-1].lower():
                palindromes.add(subarr)
    return palindromes