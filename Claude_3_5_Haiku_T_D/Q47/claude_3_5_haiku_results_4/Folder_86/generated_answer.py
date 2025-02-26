def palindromes_of_specific_lengths(s):
    if len(s) < 96:
        return set()
    substring = s[30:96]
    palindromes = set()
    for length in range(34, 56):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.lower() == candidate.lower()[::-1] and candidate.replace(' ', '').isalpha():
                palindromes.add(candidate)
    return palindromes