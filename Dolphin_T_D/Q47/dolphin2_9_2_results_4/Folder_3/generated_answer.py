def palindromes_of_specific_lengths(string):
    substr = string[27:96]
    lengths = [50, 51]
    palindromes = set()
    for length in lengths:
        for i in range(0, len(substr) - length + 1):
            candidate = substr[i:i + length]
            if all((x.isalpha() for x in candidate)) and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes