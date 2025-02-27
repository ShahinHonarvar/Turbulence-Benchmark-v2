from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(perm):
        return perm == perm[::-1]
    s = s.lower()
    substring = s[3:6]
    letters = [char for char in substring if char.isalpha()]
    unique_palindromes = set()
    for length in range(4, 7):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                unique_palindromes.add(perm_str)
    return unique_palindromes