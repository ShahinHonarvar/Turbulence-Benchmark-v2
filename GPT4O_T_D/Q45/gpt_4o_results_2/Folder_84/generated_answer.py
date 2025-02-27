from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindrome_set = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            half_length = len(perm) // 2
            if perm[:half_length] == perm[:half_length - 1:-1] or perm[:half_length] == perm[:half_length:-1]:
                palindrome_set.add(''.join(perm))
    return palindrome_set