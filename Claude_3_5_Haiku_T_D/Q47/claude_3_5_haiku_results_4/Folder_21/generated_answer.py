def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    if len(s) < 296:
        return palindromes
    substring = s[100:296]
    for length in range(136, 161):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes