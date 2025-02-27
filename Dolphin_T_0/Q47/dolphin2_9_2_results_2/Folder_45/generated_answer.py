def palindromes_of_specific_lengths(s):
    result = set()
    upper_bound = min(len(s), 140)
    lower_bound = max(70, 0)
    for i in range(lower_bound, upper_bound + 1):
        for pal_length in range(3, 61):
            if i + pal_length <= upper_bound + 1:
                piece = s[i:i + pal_length]
                if piece == piece.lower() and piece == piece.upper() and (piece == piece[::-1]):
                    result.add(piece)
    return result