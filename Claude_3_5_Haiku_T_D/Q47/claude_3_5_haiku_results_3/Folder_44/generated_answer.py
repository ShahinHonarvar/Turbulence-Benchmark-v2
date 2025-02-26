def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    substring = s[18:99]
    for length in range(31, 52):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes