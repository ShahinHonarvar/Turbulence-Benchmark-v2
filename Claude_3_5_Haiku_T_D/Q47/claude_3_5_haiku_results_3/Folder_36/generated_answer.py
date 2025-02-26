def palindromes_of_specific_lengths(s):
    palindromes = set()
    if len(s) < 284:
        return palindromes
    substring = s[124:284]
    for length in range(115, 135):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.lower() == candidate.lower()[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes