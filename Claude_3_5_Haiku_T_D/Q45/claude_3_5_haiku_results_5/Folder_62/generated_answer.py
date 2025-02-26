from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:9] if c.isalpha()]
    palindrome_set = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            candidate = ''.join(perm)
            if len(candidate) >= 7:
                for i in range(len(candidate) - length + 1):
                    substr = candidate[i:i + length]
                    if substr == substr[::-1]:
                        palindrome_set.add(substr)
    return palindrome_set