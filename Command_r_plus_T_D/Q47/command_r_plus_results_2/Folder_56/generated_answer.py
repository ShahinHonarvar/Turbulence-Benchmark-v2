def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[1:10]
    for length in range(3, 8):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment.lower() == segment[::-1].lower():
                palindromes.add(segment)
    return palindromes