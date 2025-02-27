def palindromes_of_specific_lengths(text):
    return {p for p in set([s[i:j + 1] for i in range(1, 8) for j in range(i, 8)]) if len(p) in [3, 4] and p.isalpha() and (p.lower() == p.lower()[::-1])}