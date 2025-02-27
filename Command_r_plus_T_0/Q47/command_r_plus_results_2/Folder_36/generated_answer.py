def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[123:284].lower()
    for length in range(115, 135):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment == segment[::-1] and segment.isalpha():
                palindromes.add(segment)
    return palindromes