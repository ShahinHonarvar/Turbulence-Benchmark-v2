def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[15:95]
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1]:
                clean_sub = ''.join((c for c in sub if c.isalpha()))
                clean_sub = clean_sub.lower()
                if clean_sub == clean_sub[::-1]:
                    palindromes.add(clean_sub)
    return palindromes