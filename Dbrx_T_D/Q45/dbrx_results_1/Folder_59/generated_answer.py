import string

def palindromes_between_indices(s):
    english_letters = string.ascii_letters
    substr = s[8:10].lower()
    pallette = [c for c in substr if c in english_letters]
    palindromes = {''.join(p) for p in itertools.product(pallette, repeat=3) if p == p[::-1]}
    return palindromes