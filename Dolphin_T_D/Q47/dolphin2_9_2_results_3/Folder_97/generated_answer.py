def palindromes_of_specific_lengths(s):
    substring = s[27:95]
    palindromes = set()
    for length in range(38, 50):
        for start_index in range(len(substring) - length + 1):
            piece = substring[start_index:start_index + length]
            if piece.lower() == piece.lower()[::-1]:
                clean_piece = ''.join(filter(str.isalpha, piece.lower()))
                if len(clean_piece) == length:
                    palindromes.add(clean_piece)
    return palindromes