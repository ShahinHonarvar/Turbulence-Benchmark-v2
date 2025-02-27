def palindromes_of_specific_lengths(text):
    return {w for w in text[14:91].lower().split() if 55 <= len(w) <= 71 and w == w[::-1]}