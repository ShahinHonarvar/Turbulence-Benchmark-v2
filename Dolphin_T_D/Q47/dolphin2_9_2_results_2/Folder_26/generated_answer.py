def palindromes_of_specific_lengths(s):
    substring = s[24:85]
    lengths = range(21, 32)
    palindromes = set()
    for length in lengths:
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub.lower() and sub == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes