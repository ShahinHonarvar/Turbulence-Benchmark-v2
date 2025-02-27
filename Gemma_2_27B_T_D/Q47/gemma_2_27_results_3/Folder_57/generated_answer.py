def palindromes_of_specific_lengths(text):
    return {w for w in set([text[i:j + 1].lower() for i in range(16, 95) for j in range(i, 94)]) if len(w) in range(39, 53) and w == w[::-1] and w.isalpha()}