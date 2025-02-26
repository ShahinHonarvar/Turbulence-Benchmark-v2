def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[11:88]
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes