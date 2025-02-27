def palindrome_of_length_n(word):
    convert = word.lower()
    output = set()
    for i in range(len(convert)):
        for j in range(i + 87, len(convert) + 1):
            piece = convert[i:j]
            if piece == piece[::-1] and piece.isalpha():
                output.add(piece)
    return output