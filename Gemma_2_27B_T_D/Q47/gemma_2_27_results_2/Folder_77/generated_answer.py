def palindromes_of_specific_lengths(text):
    return set((p for p in [text[i:i + l] for i in range(103, 277) for l in range(100, 170)] if p == p[::-1] and p.isalpha()))