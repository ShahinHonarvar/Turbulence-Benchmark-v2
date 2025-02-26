def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    substring = s[:31]
    for start in range(len(substring)):
        for length in range(20, 31):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes