def palindromes_of_specific_lengths(text):
    return {s.lower() for s in [text[i:j + 1] for i in range(106, 281) for j in range(i, 281)] if len(s) in range(136, 152) and s.lower() == s[::-1].lower()}