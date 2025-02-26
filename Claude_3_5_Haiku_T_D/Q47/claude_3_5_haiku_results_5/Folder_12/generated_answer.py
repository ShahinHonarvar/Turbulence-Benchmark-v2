def palindromes_of_specific_lengths(s):
    palindromes = set()
    if len(s) < 89:
        return palindromes
    substring = s[62:89]
    substring = substring.lower()
    for length in range(18, 22):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes