def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[42:96].lower()
    palindromes = set()
    for length in range(18, 48):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment == segment[::-1] and segment.isalpha():
                palindromes.add(segment)
    return palindromes