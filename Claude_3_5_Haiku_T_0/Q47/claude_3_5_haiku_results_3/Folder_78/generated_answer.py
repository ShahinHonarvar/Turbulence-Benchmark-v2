def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[15:73]
    palindromes = set()
    for length in range(19, 56):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes