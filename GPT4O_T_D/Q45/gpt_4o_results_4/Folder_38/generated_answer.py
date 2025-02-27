import itertools

def palindromes_between_indices(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = s[3:9].lower()
    letters = [char for char in s if char.isalpha()]
    result = set()
    if len(letters) < 5:
        return result
    for n in range(5, len(letters) + 1):
        for perm in itertools.permutations(letters, n):
            if is_palindrome(perm):
                result.add(''.join(perm))
    return result