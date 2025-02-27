from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = [c for c in s[:8] if c.isalpha()]
    all_combinations = set(permutations(letters, r=7))
    palindromes = {''.join(comb) for comb in all_combinations if is_palindrome(comb)}
    return palindromes