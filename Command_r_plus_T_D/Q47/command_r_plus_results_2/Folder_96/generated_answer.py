def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[100:301]
    for length in range(50, 101):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment.lower() == segment[::-1].lower() and segment.isalpha():
                palindromes.add(segment)
    return palindromes