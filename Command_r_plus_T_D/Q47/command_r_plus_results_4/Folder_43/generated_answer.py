def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[40:90].lower()
    for length in range(23, 39):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment == segment[::-1] and segment.isalpha():
                palindromes.add(segment)
    return palindromes