def palindromes_of_specific_lengths(text):
    return set((p for p in [text[i:i + l] for l in range(23, 40) for i in range(31, 75 - l)] if p == p[::-1] and p.isalpha()))