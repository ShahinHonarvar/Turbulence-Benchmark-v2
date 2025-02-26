def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[11:84].lower()
    for start in range(len(substring)):
        for length in range(37, 61):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes