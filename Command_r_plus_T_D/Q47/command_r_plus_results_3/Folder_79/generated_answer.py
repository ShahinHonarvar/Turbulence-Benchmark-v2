def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[1:9]
    for length in range(3, 5):
        for start in range(len(substring) - length + 1):
            end = start + length
            substring_piece = substring[start:end]
            if substring_piece.isalpha() and substring_piece.lower() == substring_piece[::-1].lower():
                palindromes.add(substring_piece)
    return palindromes