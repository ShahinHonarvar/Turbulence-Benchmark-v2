def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[15:95]
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes