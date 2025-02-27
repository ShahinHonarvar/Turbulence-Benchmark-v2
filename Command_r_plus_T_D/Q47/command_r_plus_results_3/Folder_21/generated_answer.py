def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[100:296]
    for length in range(136, 161):
        for start in range(len(substring) - length + 1):
            piece = substring[start:start + length]
            if piece.lower() == piece[::-1].lower() and piece.isalpha():
                palindromes.add(piece)
    return palindromes