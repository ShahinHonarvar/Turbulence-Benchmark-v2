from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join([c for c in s.lower() if c.isalpha()])
    indices = [i for i in range(len(s)) if s[i].isalpha()]
    if len(indices) < 5:
        return set()
    subset_of_letters = [s[i] for i in indices[:5]]
    permutations_of_letters = set([''.join(p) for p in permutations(subset_of_letters, 4)])
    palindromes = set()
    for p in permutations_of_letters:
        if is_palindrome(p):
            palindromes.add(p)
    return palindromes