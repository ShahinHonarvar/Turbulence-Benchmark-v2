def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[10:101]
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            substring_piece = substring[i:i + length]
            if substring_piece.lower() == substring_piece[::-1].lower():
                palindromes.add(substring_piece)
    return palindromes