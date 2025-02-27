def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[18:89]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 15, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes