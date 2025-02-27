from itertools import permutations

def palindromes_between_indices(string):
    string = string[1:6].lower()
    palindromes = set()
    for length in range(6, len(string) + 1):
        for perm in permutations(string, length):
            perm = ''.join(perm)
            if perm == perm[::-1]:
                palindromes.add(perm)
    return palindromes