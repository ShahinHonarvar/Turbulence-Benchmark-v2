import itertools

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    letters = [c for c in s[2:9] if c.isalpha()]
    ps = set()
    for i in range(7, len(letters) + 1):
        for combination in itertools.combinations(letters, i):
            for arrangement in itertools.permutations(combination):
                if is_palindrome(''.join(arrangement)):
                    ps.add(''.join(arrangement))
    return ps