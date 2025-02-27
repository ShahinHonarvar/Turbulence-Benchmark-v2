def palindromes_of_specific_lengths(text):
    return set((p for p in [text[i:i + j] for i in range(22, 96) for j in range(52, 56)] if p.isalpha() and p.lower() == p.lower()[::-1]))