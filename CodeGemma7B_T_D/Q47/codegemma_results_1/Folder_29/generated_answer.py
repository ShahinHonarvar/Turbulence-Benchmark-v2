def palindromes_of_specific_lengths(text):
    return {p for p in text[14:95].lower() if len(p) in range(18, 74) and p == p[::-1]}