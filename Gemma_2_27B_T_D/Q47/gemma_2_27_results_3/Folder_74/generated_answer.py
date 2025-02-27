def palindromes_of_specific_lengths(text):
    return {w for w in [text[i:j + 1] for i in range(30, 85) for j in range(i, 84)] if w == w[::-1] and 12 <= len(w) <= 20 and w.isalpha()}