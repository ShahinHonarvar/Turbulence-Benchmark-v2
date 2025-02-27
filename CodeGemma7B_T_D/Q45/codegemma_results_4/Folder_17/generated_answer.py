from itertools import permutations

def palindromes_between_indices(text):
    palindromes = set()
    text = text[2:7].lower()
    for p in permutations(text):
        if p[0] == p[4]:
            if p[1] == p[3]:
                palindromes.add(''.join(p))
    return palindromes