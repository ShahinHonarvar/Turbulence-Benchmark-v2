def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[12:93]
    for length in range(42, 78):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes