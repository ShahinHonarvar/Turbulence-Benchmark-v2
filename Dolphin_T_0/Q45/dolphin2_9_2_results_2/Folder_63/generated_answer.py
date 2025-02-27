from itertools import permutations

def palindromes_between_indices(s):
    English_letters = [c for c in s if c.isalpha()]
    if len(set(English_letters)) != len(English_letters):
        return set()
    palindrome_set = set()
    for p in permutations(English_letters, 3):
        pal = ''.join(p)
        if pal == pal[::-1]:
            palindrome_set.add(pal)
    return palindrome_set