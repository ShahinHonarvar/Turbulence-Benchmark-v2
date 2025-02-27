def palindromes_between_indices(s):
    letters = s[1:6].lower()
    palindromes = set()
    for perm in permutations(letters):
        if len(perm) >= 4 and perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return palindromes