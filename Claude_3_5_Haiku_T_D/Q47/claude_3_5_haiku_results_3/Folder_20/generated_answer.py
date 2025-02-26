def palindromes_of_specific_lengths(s):
    if len(s) <= 74:
        return set()
    substring = s[20:75]
    palindromes = set()
    for length in range(36, 43):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes