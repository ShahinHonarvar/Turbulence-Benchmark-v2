def palindromes_of_specific_lengths(string):
    substring = string[30:75]
    palindromes = set()
    for length in range(23, 40):
        for i in range(len(substring)):
            region = substring[i:i + length]
            if region == region.lower() or region == region.upper():
                if region == region[::-1]:
                    palindromes.add(region)
    return palindromes