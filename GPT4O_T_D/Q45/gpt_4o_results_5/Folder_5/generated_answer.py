from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for perm in permutations(s):
        if len(perm) >= 4:
            for start in range(len(perm) - 3):
                for end in range(start + 4, len(perm) + 1):
                    substr = perm[start:end]
                    if substr == substr[::-1]:
                        palindromes.add(''.join(substr))
    return palindromes