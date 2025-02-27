def palindromes_of_specific_lengths(text):
    return set((p for p in [text[i:j].lower() for i in range(18, 88) for j in range(i + 38, min(i + 61, 88) + 1)] if p == p[::-1] and p.isalpha()))