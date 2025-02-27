def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[100:200]
    for length in range(5, 11):
        for start in range(len(substring) - length + 1):
            piece = substring[start:start + length]
            if piece.lower() == piece[::-1].lower():
                palindromes.add(piece)
    return palindromes