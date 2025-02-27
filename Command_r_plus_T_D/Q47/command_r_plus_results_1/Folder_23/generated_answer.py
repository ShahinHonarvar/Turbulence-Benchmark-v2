def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    substring = s[22:95]
    palindromes = set()
    for length in range(17, 56):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes