import itertools

def palindromes_between_indices(s):
    letters = s[1:5]
    arrangements = list(itertools.permutations(letters, len(letters)))
    arrangements = [''.join(arr.lower()) for arr in arrangements]
    palindromes = set(filter(lambda p: len(p) >= 3 and p == p[::-1], arrangements))
    return palindromes