def palindromes_of_specific_lengths(string):
    substring = string[12:100]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            sub = substring[i:j]
            if 26 <= len(sub) <= 29:
                lower_sub = sub.lower()
                if lower_sub == lower_sub[::-1]:
                    palindromes.add(sub)
    return palindromes