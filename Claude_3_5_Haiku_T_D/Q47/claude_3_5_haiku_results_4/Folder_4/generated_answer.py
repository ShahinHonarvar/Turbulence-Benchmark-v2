def palindromes_of_specific_lengths(s):
    palindromes = set()
    if len(s) < 93:
        return palindromes
    substring = s[12:93].lower()
    for length in range(17, 67):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((char.isalpha() for char in candidate)) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes