import itertools

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == ''.join(reversed(s))
    s = s[:6].lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = set()
    for i in range(4, len(s) + 1):
        for comb in itertools.combinations(s, i):
            for p in itertools.permutations(comb):
                word = ''.join(p)
                if is_palindrome(word) and set(word).issubset(set(alphabet)):
                    result.add(word)
    return result