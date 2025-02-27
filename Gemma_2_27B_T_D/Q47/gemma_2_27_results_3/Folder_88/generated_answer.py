def palindromes_of_specific_lengths(text):
    return set((p for p in [w.lower() for w in text[11:88].split() if len(w) in range(4, 6) and w.isalpha()] if p == p[::-1]))