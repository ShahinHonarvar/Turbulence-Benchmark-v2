def palindromes_between_indices(s):
    return {''.join(p) for p in product(*zip(*[filter(str.ascii_letters, s[i:j + 1].lower()) for i, j in [(3, 5)]]))}