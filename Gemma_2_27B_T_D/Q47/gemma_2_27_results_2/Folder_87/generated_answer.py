def palindromes_of_specific_lengths(text):
    return {p for p in set([text[i:j + 1].lower() for i in range(11, 94) for j in range(i, 93)]) if len(p) in range(34, 55) and p == p[::-1] and p.isalpha()}