from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    letters = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for perm in permutations(letters):
        joined_perm = ''.join(perm)
        if joined_perm == joined_perm[::-1] and len(joined_perm) >= 7:
            palindromes.add(joined_perm)
    return palindromes