from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    substring = s[3:7].lower()
    valid_chars = [char for char in substring if char.isalpha()]
    if len(valid_chars) < 4:
        return set()
    palindrome_set = set()
    for perm in set(permutations(valid_chars, 4)):
        for length in range(4, len(perm) + 1):
            for p in set(permutations(perm, length)):
                forward = ''.join(p)
                backward = forward[::-1]
                if forward == backward:
                    palindrome_set.add(forward)
    return palindrome_set