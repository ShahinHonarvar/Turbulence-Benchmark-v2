from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[7:10] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 1, len(perm) + 1):
                subset = perm[i:j]
                if len(subset) >= 3:
                    candidate = subset + subset[::-1]
                    if len(candidate) % 2 == 0:
                        mid = len(candidate) // 2
                        candidate = candidate[:mid] + candidate[mid - 1::-1]
                    palindrome_set.add(''.join(candidate))
    return palindrome_set