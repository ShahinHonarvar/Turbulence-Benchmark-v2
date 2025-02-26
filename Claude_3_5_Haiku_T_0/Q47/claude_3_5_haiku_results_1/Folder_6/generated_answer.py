def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[45:99].lower()
    for length in range(40, 48):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if len(candidate) == length and candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes