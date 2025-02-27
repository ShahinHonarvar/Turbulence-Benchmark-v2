def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[11:93]
    palindromes = set()
    for length in range(42, 78):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes