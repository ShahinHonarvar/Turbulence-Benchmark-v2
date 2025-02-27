def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(136, 161):
        for i in range(100, 296 - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)):
                lower_sub = substring.lower()
                if lower_sub == lower_sub[::-1]:
                    palindromes.add(substring)
    return palindromes