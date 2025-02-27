from functools import reduce
    from itertools import combinations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def build_string(idx):
        return s[idx[0]:idx[1] + 1]

    def create_permutations(lst, r):
        return lst[:r] + combinations(lst, r)
    english_letters = [c for c in s[3:6] if c.isalpha()]
    if len(english_letters) < 4:
        return set()
    permutations = reduce(create_permutations, [english_letters] * min(len(english_letters), 4))
    palindromes = {reduce(lambda x, y: x + y, p) for p in permutations if is_palindrome(reduce(lambda x, y: x + y, p))}
    return palindromes