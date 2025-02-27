from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    english_letters = [c for c in s[1:8] if c.isalpha()]
    palindromes_set = set()
    for perm in permutations(english_letters):
        for length in range(7, len(perm) + 1):
            candidate = ''.join(perm[:length])
            if is_palindrome(candidate):
                palindromes_set.add(candidate)
    return palindromes_set