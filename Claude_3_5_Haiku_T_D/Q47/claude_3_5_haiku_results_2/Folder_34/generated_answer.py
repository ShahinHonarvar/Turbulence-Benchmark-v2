def palindromes_of_specific_lengths(s):
    if len(s) < 301:
        return set()
    substring = s[200:301].lower()
    palindromes = set()
    for length in range(10, 51):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes