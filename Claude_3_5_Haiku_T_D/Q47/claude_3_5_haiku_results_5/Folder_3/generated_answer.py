def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[27:96]
    for length in range(49, 52):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha():
                lowered = candidate.lower()
                if lowered == lowered[::-1]:
                    palindromes.add(candidate)
    return palindromes