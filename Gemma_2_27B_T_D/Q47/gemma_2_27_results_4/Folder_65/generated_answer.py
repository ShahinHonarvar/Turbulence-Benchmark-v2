def palindromes_of_specific_lengths(text):
    return set((p for p in [text[i:i + j] for i in range(15, 96) for j in range(20, 67)] if p == p[::-1] and p.isalpha()))