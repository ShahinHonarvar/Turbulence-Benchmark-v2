def palindromes_of_specific_lengths(s: str) -> set[str]:
    substring = s[39:95].lower()
    palindromes = set()
    for length in range(14, 53):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment == segment[::-1] and segment.isalpha():
                palindromes.add(segment)
    return palindromes