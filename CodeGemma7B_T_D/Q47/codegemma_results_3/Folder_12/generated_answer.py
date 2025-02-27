from itertools import combinations_with_replacement as comb_wr

def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = text[62:89]
    return {''.join(candidate) for candidate in comb_wr(text, range(18, 22)) if ''.join(candidate) == ''.join(candidate)[::-1]}