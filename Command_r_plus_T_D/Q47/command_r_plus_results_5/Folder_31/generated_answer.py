def palindromes_of_specific_lengths(s: str) -> set[str]:
    substring = s[10:84]
    palindromes = set()
    for length in range(37, 61):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment.lower() == segment[::-1].lower() and segment.isalpha():
                palindromes.add(segment)
    return palindromes