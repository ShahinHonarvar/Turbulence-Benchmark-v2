from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(p):
        return p == p[::-1]
    s = s[:5].lower()
    letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    if len(letters) < 3:
        return palindromes
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            p = ''.join(perm)
            if is_palindrome(p):
                palindromes.add(p)
    return palindromes