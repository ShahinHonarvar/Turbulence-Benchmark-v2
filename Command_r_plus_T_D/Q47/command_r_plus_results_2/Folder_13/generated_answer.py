def palindromes_of_specific_lengths(s: str) -> set[str]:
    substring = s[12:96]
    palindromes = set()
    for length in range(57, 61):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment.lower() == segment[::-1].lower():
                palindromes.add(segment)
    return palindromes