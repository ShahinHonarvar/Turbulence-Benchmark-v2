from itertools import permutations

def palindromes_between_indices(s):
    letters_in_range = [c.lower() for c in s[4:10] if c.isalpha()]
    if len(letters_in_range) < 7:
        return set()
    palindromes = set()
    for perm in set(permutations(letters_in_range, 7)):
        half_length = len(perm) // 2
        left_half = perm[:half_length]
        center = perm[half_length] if len(perm) % 2 != 0 else ''
        right_half = perm[half_length + len(perm) % 2:][::-1]
        palindrome = ''.join(list(left_half) + list(center) + list(right_half))
        palindromes.add(palindrome)
    return palindromes