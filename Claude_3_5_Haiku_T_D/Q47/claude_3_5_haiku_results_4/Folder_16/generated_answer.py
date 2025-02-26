def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    substring = s[15:87]
    for length in range(51, 61):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes