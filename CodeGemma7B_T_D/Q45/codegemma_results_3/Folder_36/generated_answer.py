import itertools

def palindromes_between_indices(string):
    alphabets = string[5:9]
    english_letters = spellings = [''.join(p) for i in range(len(alphabets)) for p in itertools.permutations(sorted(alphabets[i]))]
    return {p for p in spellings if p[0] in 'AEIOU' and p[-1] in 'AEIOU'}