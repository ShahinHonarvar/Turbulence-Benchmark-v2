def palindromes_of_specific_lengths(s):
    substring = s[10:96]
    palindromes = set()
    for length in range(45, 53):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if all((c.isalpha() for c in sub)) and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes