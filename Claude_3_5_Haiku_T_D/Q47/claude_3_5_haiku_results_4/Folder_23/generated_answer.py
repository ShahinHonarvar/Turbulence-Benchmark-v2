def palindromes_of_specific_lengths(s):
    if len(s) < 95:
        return set()
    substring = s[23:95].lower()
    palindromes = set()
    for length in range(17, 56):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if len(candidate) >= 17 and len(candidate) <= 55:
                if candidate == candidate[::-1] and candidate.isalpha():
                    palindromes.add(candidate)
    return palindromes