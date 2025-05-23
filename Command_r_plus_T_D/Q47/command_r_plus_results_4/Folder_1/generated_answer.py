def palindromes_of_specific_lengths(s: str) -> set[str]:
    substring = s[14:90].lower()
    palindromes = set()
    for length in range(40, 73):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes