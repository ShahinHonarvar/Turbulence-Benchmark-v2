from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[4:7].lower()
    letters = [ch for ch in substring if ch.isalpha()]
    possible_palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                possible_palindromes.add(candidate)
    return possible_palindromes