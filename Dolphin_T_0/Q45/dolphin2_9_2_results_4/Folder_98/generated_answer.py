from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s[3:6].lower()
    letter_set = set(ascii_lowercase)
    results = set()
    for p in permutations(s, len(s)):
        palindromes = [''.join(p[i:j]) for i in range(len(p)) for j in range(i + 3, len(p) + 1)]
        palindromes = [x for x in palindromes if set(x).issubset(letter_set)]
        for q in permutations(p, len(p)):
            y = ''.join(q)
            if y in palindromes:
                results.add(y)
    return results