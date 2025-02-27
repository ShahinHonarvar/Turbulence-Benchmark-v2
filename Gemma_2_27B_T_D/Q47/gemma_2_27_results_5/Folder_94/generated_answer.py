def palindromes_of_specific_lengths(text):
    return set((p for p in text[40:95].lower() if len(p) in range(45, 52) and p == p[::-1] and p.isalpha()))