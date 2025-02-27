def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[29:97]
    palindromes = set()
    for length in range(12, 19):
        for i in range(len(substring) - length + 1):
            substring_piece = substring[i:i + length]
            if substring_piece.lower() == substring_piece[::-1].lower():
                palindromes.add(substring_piece)
    return palindromes