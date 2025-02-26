def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[125:284].lower()
    for length in range(109, 127):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes