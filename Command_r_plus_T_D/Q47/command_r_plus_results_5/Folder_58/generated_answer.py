def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[124:284]
    for length in range(109, 127):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate[::-1].lower() and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes