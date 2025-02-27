def palindromes_of_specific_lengths(text):
    return set((p for p in [text[i:i + l] for i in range(155, 284) for l in range(104, 121)] if p == p[::-1] and p.isalpha()))