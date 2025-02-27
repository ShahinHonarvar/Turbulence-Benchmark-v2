from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[4:9].lower()
    letters = [char for char in sub_str if char.isalpha()]
    palindromes_set = set()
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindromes_set.add(''.join(perm))
    return palindromes_set