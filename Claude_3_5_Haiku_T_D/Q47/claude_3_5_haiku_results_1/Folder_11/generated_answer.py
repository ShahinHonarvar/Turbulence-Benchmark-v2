def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[24:98]
    palindromes = set()
    for length in range(10, 37):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if len(candidate) == length and candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes