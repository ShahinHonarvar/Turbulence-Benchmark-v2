def palindromes_of_specific_lengths(s):
    substring = s[28:95]
    palindromes = set()
    for length in range(38, 50):
        for i in range(len(substring)):
            if substring[i:i + length].lower() == substring[i:i + length].lower()[::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes