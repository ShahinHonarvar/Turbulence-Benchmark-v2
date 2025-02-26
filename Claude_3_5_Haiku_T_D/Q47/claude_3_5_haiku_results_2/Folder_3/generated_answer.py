def palindromes_of_specific_lengths(s):
    if len(s) < 96:
        return set()
    substring = s[27:96].lower()
    palindromes = set()
    for start in range(len(substring)):
        for length in range(49, 52):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if all((c.isalpha() for c in candidate)) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes