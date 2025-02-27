def palindromes_of_specific_lengths(s):
    substring = s[16:61]
    palindromes = set()
    for length in range(16, 40):
        for i in range(len(substring) - length + 1):
            if all((c.isalpha() for c in substring[i:i + length])):
                lower_substring = substring[i:i + length].lower()
                if lower_substring == lower_substring[::-1]:
                    palindromes.add(substring[i:i + length])
    return palindromes