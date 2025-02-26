def palindromes_of_specific_lengths(s):
    palindromes = set()
    if len(s) < 91:
        return palindromes
    substring = s[34:91].lower()
    for length in range(14, 40):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if len(candidate) == length and candidate.isalpha() and (candidate == candidate[::-1]):
                palindromes.add(candidate)
    return palindromes