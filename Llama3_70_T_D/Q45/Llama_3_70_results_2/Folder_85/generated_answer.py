from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substr = s[2:9]
    letters = [char for char in substr if char.isalpha()]
    result = set()
    for perm in permutations(letters, 7):
        palindrome = ''.join(perm) + perm[-2::-1]
        result.add(palindrome)
    for perm in permutations(letters, 8):
        palindrome = ''.join(perm) + perm[-2::-1]
        result.add(palindrome)
    return result