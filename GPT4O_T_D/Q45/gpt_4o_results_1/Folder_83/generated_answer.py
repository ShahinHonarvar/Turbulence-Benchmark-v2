from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    english_letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for p in permutations(english_letters, len(english_letters)):
        if p == p[::-1] and len(p) >= 7:
            palindromes.add(''.join(p))
    return palindromes