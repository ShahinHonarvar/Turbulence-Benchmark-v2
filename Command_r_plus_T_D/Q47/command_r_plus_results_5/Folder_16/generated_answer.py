def palindromes_of_specific_lengths(s: str) -> set[str]:
    substring = s[14:87].lower()
    palindromes = set()
    for i in range(len(substring) - 50):
        for length in range(51, 61):
            if i + length > len(substring):
                break
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes