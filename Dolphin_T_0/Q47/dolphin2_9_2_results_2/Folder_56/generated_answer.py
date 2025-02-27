def palindromes_of_specific_lengths(s):
    sub = s[1:10]
    palindromes = set()
    for length in range(3, 8):
        for i in range(len(sub) - length + 1):
            piece = sub[i:i + length]
            if all((c.isalpha() for c in piece)) and piece.lower() == piece.lower()[::-1]:
                palindromes.add(piece)
    return palindromes