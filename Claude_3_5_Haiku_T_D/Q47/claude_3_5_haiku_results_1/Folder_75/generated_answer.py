def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[31:75].lower()
    for length in range(23, 40):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes