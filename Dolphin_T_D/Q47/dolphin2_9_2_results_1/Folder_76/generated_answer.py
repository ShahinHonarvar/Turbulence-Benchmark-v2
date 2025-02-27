def palindromes_of_specific_lengths(s):
    sub_string = s[101 - 1:292]
    palindromes_set = set()
    for length in range(154, 183):
        for i in range(len(sub_string) - length + 1):
            piece = sub_string[i:i + length]
            if piece.lower() == piece[::-1].lower():
                palindromes_set.add(piece)
    return palindromes_set