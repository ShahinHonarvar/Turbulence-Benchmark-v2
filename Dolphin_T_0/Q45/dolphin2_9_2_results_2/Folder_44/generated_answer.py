import string

def palindromes_between_indices(s):
    letters_between = s[2:8].lower()
    palindromes = set()
    permutations = [''.join(p) for p in permutations(letters_between)]
    for p in permutations:
        if p == p[::-1] and len(p) >= 3:
            palindromes.add(p)
    return palindromes