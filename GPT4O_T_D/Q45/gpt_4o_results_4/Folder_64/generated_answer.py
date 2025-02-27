from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[4:10].lower()
    filtered_letters = ''.join(filter(str.isalpha, substring))
    if len(filtered_letters) < 5:
        return set()
    palindromes = set()
    for i in range(5, len(filtered_letters) + 1):
        for perm in permutations(filtered_letters, i):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes