def palindromes_of_specific_lengths(text):
    return {w.lower() for w in set(text[15:95].lower().split()) if len(w) in range(18, 74) and w.lower() == w.lower()[::-1] and w.isalpha()}