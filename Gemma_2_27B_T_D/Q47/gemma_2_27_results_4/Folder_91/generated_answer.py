def palindromes_of_specific_lengths(text):
    return {w for w in set(text[0:11].lower()[:].split()) if len(w) in range(3, 6) and w == w[::-1] and w.isalpha()}