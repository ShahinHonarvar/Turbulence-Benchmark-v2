def palindromes_of_specific_lengths(s):
    substring = s[100:301]
    palindromes = set()
    for length in range(50, 101):
        for i in range(len(substring) - length + 1):
            sublim = substring[i:i + length]
            lower_sublim = sublim.lower()
            if lower_sublim == lower_sublim[::-1] and lower_sublim.isalpha():
                palindromes.add(sublim)
    return palindromes