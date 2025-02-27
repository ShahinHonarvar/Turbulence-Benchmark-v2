from itertools import permutations

def palindromes_between_indices(s):
    s_section = s[1:5].lower()
    letters = [c for c in s_section if c.isalpha()]
    palindromes_set = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindromes_set.add(''.join(perm))
    return palindromes_set