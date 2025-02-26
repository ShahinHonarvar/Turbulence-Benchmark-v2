def palindromes_of_specific_lengths(s):
    if len(s) < 71:
        return set()
    substring = s[63:71].lower()
    palindromes = set()
    for length in range(4, 6):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes