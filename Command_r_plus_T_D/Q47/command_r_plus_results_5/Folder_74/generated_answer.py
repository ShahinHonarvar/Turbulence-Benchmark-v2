def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[30:85]
    palindromes = set()
    for length in range(12, 21):
        for i in range(len(substring) - length + 1):
            substring_piece = substring[i:i + length]
            if substring_piece.isalpha() and substring_piece.lower() == substring_piece[::-1].lower():
                palindromes.add(substring_piece)
    return palindromes