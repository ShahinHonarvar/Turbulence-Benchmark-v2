def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]

    def get_combinations(s):
        n = len(s)
        return sum([list(itertools.combinations(s, r)) for r in range(n + 1)], [])
    combined = ''.join(sorted(s[1:7]))
    palindromes = set()
    for r in range(4, 7):
        for c in get_combinations(combined):
            c = ''.join(sorted(c))
            if len(c) == r and is_palindrome(c):
                palindromes.add(c)
    return palindromes