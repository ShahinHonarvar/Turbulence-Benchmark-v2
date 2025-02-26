def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    substring = s[11:88]
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes