def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[36:93]
    for length in range(10, 36):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length].lower()
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes