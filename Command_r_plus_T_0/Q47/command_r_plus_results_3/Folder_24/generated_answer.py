def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[11:93].lower()
    for length in range(42, 78):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes