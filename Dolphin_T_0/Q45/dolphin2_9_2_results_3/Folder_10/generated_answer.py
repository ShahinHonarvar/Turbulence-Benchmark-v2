from itertools import permutations

def palindromes_between_indices(s):

    def get_palindromes(s):
        res = set()
        for p in permutations(s):
            if len(p) >= 3 and p == p[::-1]:
                res.add(''.join(p).lower())
        return res
    res = get_palindromes(''.join(sorted(s[0:6])))
    return res