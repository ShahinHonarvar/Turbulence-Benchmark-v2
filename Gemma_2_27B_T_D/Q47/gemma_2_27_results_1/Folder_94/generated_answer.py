def palindromes_of_specific_lengths(text):
    return {s for s in set([text[i:j + 1].lower() for i in range(40, 95) for j in range(i, 95)]) if len(s) in range(45, 52) and s == s[::-1] and s.isalpha()}