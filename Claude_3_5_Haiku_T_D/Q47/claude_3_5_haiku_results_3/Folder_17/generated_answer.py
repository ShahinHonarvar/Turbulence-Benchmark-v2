def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[22:96]
    for start in range(len(substring)):
        for length in range(52, 56):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if len(candidate) not in range(52, 56):
                continue
            if not all((char.isalpha() for char in candidate)):
                continue
            if candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes