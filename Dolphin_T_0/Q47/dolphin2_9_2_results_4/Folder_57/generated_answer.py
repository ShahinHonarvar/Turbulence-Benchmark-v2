def palindromes_of_specific_lengths(s):
    substring = s[16:95]
    palindromes = set()
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if all((c.isalpha() or not c.isalpha() for c in sub)):
                if sub == sub[::-1]:
                    palindromes.add(sub.lower())
    return palindromes