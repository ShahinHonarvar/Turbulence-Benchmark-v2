def palindromes_of_specific_lengths(s):
    if len(s) < 97:
        return set()
    substring = s[29:97].lower()
    palindromes = set()
    for start in range(len(substring)):
        for length in range(12, 19):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes