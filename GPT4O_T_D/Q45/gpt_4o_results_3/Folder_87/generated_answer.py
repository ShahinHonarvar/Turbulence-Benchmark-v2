from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:10].lower()
    filtered_chars = [ch for ch in s if ch.isalpha()]
    palindromes_set = set()
    for i in range(3, len(filtered_chars) + 1):
        for perm in set(permutations(filtered_chars, i)):
            if perm == perm[::-1]:
                palindromes_set.add(''.join(perm))
    return palindromes_set