from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join(filter(lambda c: c in ascii_letters, s[:8])).lower()
    all_combinations = set((''.join(p) for i in range(7, len(substring) + 1) for p in permutations(substring, i)))
    palindromes = {word for word in all_combinations if is_palindrome(word)}
    return palindromes