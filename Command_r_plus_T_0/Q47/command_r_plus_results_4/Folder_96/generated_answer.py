def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[100:301]
    for length in range(50, 101):
        for i in range(len(substring) - length):
            segment = substring[i:i + length]
            if segment.lower() == segment[::-1].lower():
                palindromes.add(segment)
    return palindromes