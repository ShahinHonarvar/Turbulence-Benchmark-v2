def palindromes_of_specific_lengths(text):
    return {p for p in set((i for start in range(1, 10 - i + 1) for i in range(3, 8) if (p := text[start:start + i].lower()) == p[::-1] and p.isalpha()))}