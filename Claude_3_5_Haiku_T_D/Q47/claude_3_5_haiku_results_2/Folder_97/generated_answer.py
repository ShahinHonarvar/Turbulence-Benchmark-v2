def palindromes_of_specific_lengths(s):
    palindromes = set()
    substr = s[28:95]
    for length in range(38, 50):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if len(candidate) == length and all((char.isalpha() for char in candidate)):
                lowercase_candidate = candidate.lower()
                if lowercase_candidate == lowercase_candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes