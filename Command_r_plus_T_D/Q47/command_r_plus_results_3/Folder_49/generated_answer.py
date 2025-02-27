def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[10:101]
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            substring_piece = substring[i:i + length]
            if substring_piece.isalpha() and substring_piece.lower() == substring_piece[::-1].lower():
                palindromes.add(substring_piece)
    return palindromes