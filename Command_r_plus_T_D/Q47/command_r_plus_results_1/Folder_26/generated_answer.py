def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[23:85].lower()
    for length in range(21, 32):
        for i in range(len(substring) - length + 1):
            substring_piece = substring[i:i + length]
            if substring_piece == substring_piece[::-1] and substring_piece.isalpha():
                palindromes.add(substring_piece)
    return palindromes