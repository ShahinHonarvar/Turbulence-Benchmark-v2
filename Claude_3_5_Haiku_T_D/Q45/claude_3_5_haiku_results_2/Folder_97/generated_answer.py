from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:5] if c.isalpha()]
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 3, len(perm) + 1):
                subset = perm[i:j]
                if len(subset) >= 3:
                    candidate = subset + subset[::-1]
                    palindrome = ''.join(candidate)
                    if palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes