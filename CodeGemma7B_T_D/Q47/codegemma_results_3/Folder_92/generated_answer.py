from nltk.metrics.distance import edit_distance

def palindromes_of_specific_lengths(txt):
    return {p for p in txt.lower() if len(p) in range(3, 5) and p == p[::-1] and (edit_distance(p, 'radar', 1) <= 1) and (txt.lower().index(p) in range(5))}