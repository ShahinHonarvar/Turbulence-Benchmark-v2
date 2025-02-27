def palindromes_of_specific_lengths(s):
    substring = s[34:91]
    palindromes = set()
    for length in range(14, 40):
        for index in range(len(substring) - length + 1):
            sub = substring[index:index + length]
            if all((c.isalpha() for c in sub)):
                if sub.lower() == sub[::-1].lower():
                    palindromes.add(sub)
    return palindromes