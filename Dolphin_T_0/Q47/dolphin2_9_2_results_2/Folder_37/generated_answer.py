def palindromes_of_specific_lengths(string):
    sub_string = string[:10]
    palindromes = set()
    for length in range(3, 6):
        for i in range(len(sub_string) - length + 1):
            piece = sub_string[i:i + length]
            if piece == piece.lower() and piece == piece[::-1].lower():
                palindromes.add(piece)
    return palindromes