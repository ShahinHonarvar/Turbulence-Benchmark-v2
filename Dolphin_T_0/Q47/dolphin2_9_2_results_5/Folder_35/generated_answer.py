def palindromes_of_specific_lengths(s):
    substring = s[33:91]
    palindromes_set = set()
    for length in range(14, 40):
        for i in range(len(substring) - length + 1):
            piece = substring[i:i + length]
            if piece.lower() == piece.lower()[::-1] and piece.isalpha():
                palindromes_set.add(piece)
    return palindromes_set if palindromes_set else None