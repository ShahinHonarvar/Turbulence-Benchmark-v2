def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[13:96]
    for length in range(57, 61):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate[::-1].lower() and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes