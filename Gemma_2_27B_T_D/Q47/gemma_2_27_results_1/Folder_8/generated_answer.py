def palindromes_of_specific_lengths(text):
    return set((p for p in (text[17:73] for text in [text.lower()]) if p == p[::-1] and 50 <= len(p) <= 51 and all((c.isalpha() for c in p))))