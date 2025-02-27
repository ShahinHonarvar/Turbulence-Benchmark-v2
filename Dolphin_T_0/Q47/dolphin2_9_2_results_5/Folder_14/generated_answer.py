def palindromes_of_specific_lengths(s):
    substring = s[10:75]
    palindromes = set()
    for length in range(6, 9):
        for i in range(len(substring) - length + 1):
            p = substring[i:i + length]
            if all((c.isalpha() for c in p.lower())) and p.lower() == p.lower()[::-1]:
                palindromes.add(p)
    return palindromes