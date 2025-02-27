def palindromes_of_specific_lengths(text):
    return set((p for p in [text[i:i + l] for i in range(63, 71) for l in range(4, 6) if text[i:i + l] == text[i:i + l][::-1] and p.isalpha()]))