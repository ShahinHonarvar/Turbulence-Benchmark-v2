from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:10] if c.isalpha()]
    palindrome_set = set()
    if len(letters) < 4:
        return palindrome_set
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 3, len(perm) + 1):
                subset = perm[i:j]
                if len(subset) >= 4:
                    candidate = subset + subset[::-1]
                    if len(set(candidate)) == len(subset):
                        palindrome_set.add(''.join(candidate))
    return palindrome_set