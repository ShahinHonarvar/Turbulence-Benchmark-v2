def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[:8]
    for start in range(len(substring)):
        for length in [4, 5]:
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes