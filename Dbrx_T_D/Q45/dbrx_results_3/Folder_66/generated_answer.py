import string

def palindromes_between_indices(s):
    s = s.lower()
    chars = [c for c in s if c in string.ascii_letters][:6]
    if len(chars) < 5:
        return set()
    palindromes = {p for p in [''.join(t) for t in itertools.product(chars, repeat=5)] if p == p[::-1]}
    return palindromes