def palindromes_of_specific_lengths(s):
    substring = s[105:281]
    lengths = range(136, 152)
    palindromes = set()
    for length in lengths:
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub.lower()[::-1] and all((c.isalpha() for c in sub)):
                palindromes.add(sub)
    return palindromes