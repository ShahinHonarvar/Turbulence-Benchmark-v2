from itertools import permutations, chain

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    alphabet = set(s) & set('abcdefghijklmnopqrstuvwxyz')
    pals = set(chain.from_iterable((permutations(''.join(alphabet), r) for r in range(5, len(''.join(alphabet)) + 1))))
    return {p for p in pals if is_palindrome(p)}