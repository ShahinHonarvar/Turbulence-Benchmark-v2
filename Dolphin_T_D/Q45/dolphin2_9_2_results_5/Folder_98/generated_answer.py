def palindromes_between_indices(s):
    subs = s[3:6]
    result = set()
    for p in range(4, len(subs) + 1):
        for i in range(len(subs) - p + 1):
            subs_piece = subs[i:i + p]
            if subs_piece == subs_piece[::-1]:
                result.add(subs_piece.lower())
    return result