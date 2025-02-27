def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[100:301]
    for length in range(50, 101):
        for start in range(len(substring) - length):
            piece = substring[start:start + length]
            if piece.lower() == piece[::-1].lower():
                palindromes.add(piece)
    return palindromes