def palindromes_of_specific_lengths(s):
    substring = s[31:75]
    palindromes = set()
    for length in range(23, 40):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes