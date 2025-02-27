import itertools

def palindromes_between_indices(string):
    s = set()
    for p in itertools.permutations(string[1:5]):
        combined = ''.join(p)
        if len(combined) >= 5 and combined.lower() == combined[::-1].lower():
            s.add(combined.lower())
    return s