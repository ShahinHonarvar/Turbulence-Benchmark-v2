def palindromes_of_specific_lengths(text):
    return {w.lower() for w in set(text[2:9]) if w.lower() == w[::-1].lower() and 3 <= len(w) <= 4 and w.isalpha()}