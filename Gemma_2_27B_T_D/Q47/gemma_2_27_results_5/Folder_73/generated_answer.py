def palindromes_of_specific_lengths(text):
    return {s for s in set([text[i:j + 1].lower() for i in range(21, 63) for j in range(i, 62)]) if len(s) in range(22, 34) and s == s[::-1] and s.isalpha()}