def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[10:84]
    for length in range(13, 67):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes