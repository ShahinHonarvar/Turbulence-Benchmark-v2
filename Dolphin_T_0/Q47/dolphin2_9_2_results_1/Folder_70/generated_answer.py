def palindromes_of_specific_lengths(s):
    substring = s[9:71]
    palindromes = set()
    for i in range(10, len(substring) - 23):
        for length in range(24, min(len(substring) - i + 1, 53)):
            sub = substring[i:i + length]
            if all((c.isalpha() for c in sub.lower())) and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes