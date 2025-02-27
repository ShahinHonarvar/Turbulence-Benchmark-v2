def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[15:78].lower()
    for length in range(43, 48):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment == segment[::-1] and segment.isalpha():
                palindromes.add(segment)
    return palindromes