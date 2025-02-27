def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[16:96]
    for length in range(13, 50):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment.isalpha() and segment.lower() == segment[::-1].lower():
                palindromes.add(segment)
    return palindromes