def palindromes_of_specific_lengths(text):
    return {p for p in set([text[i:i + t] for t in range(12, 21) for i in range(30, 85 - t + 1)]) if p == p[::-1] and p.isalpha()}