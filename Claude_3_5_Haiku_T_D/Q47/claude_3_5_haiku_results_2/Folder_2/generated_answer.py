def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[10:60]
    palindromes = set()
    for length in range(18, 37):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes