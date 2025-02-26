def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[15:73].lower()
    for length in range(19, 56):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if len(candidate) == length and candidate.isalpha() and (candidate == candidate[::-1]):
                palindromes.add(candidate)
    return palindromes