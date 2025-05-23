def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[100:296]
    palindromes = set()
    for length in range(136, 161):
        for start in range(len(substring) - length + 1):
            piece = substring[start:start + length]
            if piece.lower() == piece[::-1].lower():
                palindromes.add(piece)
    return palindromes