def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    letters = [c.lower() for c in s[2:8] if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for sub in set((''.join(p) for p in itertools.permutations(letters, r))):
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes