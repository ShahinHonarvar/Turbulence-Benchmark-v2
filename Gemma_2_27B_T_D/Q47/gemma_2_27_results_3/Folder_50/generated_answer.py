def palindromes_of_specific_lengths(text):
    return {p for p in [text[i:i + l] for l in range(10, 36) for i in range(36, 93 - l)] if p == p[::-1] and p.isalpha()}