def palindromes_of_specific_lengths(s):
    s = s[15:95]
    palindromes = set()
    for length in range(39, 53):
        subs = [s[i:i + length].lower() for i in range(len(s) - length + 1)]
        palindromes |= set(filter(lambda x: all((c.isalpha() for c in x)), subs))
    return palindromes