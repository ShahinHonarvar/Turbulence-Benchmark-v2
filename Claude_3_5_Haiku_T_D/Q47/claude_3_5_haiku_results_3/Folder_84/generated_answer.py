def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    if len(s) < 78:
        return palindromes
    substring = s[23:78]
    for length in range(13, 41):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((char.isalpha() for char in candidate)) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes