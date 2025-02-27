def palindromes_of_specific_lengths(text):
    return {p for p in {text[i:j + 1].lower() for i in range(18, 88) for j in range(i, 87)} if len(p) in range(38, 61) and p == p[::-1] and p.isalpha()}