from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    letters = [c for c in s[1:8].lower() if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            sub = ''.join(perm)
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes