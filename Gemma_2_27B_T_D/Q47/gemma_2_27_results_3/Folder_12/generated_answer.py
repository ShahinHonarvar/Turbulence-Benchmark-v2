def palindromes_of_specific_lengths(text):
    return set((p for p in [text[i:i + l].lower() for l in range(18, 22) for i in range(62, 89 - l + 1)] if p == p[::-1] and p.isalpha()))