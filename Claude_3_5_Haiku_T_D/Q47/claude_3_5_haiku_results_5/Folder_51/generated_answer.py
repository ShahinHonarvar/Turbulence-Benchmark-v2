def palindromes_of_specific_lengths(s):
    if len(s) < 9:
        return set()
    substring = s[2:9]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes