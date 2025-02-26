def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[3:301]
    palindromes = set()
    for length in range(30, 301):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and all((char.isalpha() for char in candidate)):
                palindromes.add(candidate)
    return palindromes