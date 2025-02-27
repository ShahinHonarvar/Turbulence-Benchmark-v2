def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[40:95].lower()
    palindromes = set()
    for length in range(45, 52):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment == segment[::-1] and segment.isalpha():
                palindromes.add(segment)
    return palindromes