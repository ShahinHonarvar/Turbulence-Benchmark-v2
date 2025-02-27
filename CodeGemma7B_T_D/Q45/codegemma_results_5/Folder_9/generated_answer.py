from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    result = set()
    for perm in permutations(s):
        substring = ''.join(perm[0:7])
        if is_palindrome(substring) and len(substring) >= 7:
            result.add(substring)
    return result