def palindromes_of_specific_lengths(s):
    substring = s[30:75]
    palindromes = set()
    for length in range(23, 40):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if all((c.isalpha() for c in sub)):
                lower_sub = sub.lower()
                if lower_sub == lower_sub[::-1]:
                    palindromes.add(sub)
    return palindromes