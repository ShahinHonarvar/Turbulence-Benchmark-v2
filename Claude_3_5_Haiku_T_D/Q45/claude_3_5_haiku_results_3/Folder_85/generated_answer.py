from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c.isalpha()]
    palindrome_set = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            sorted_perm = sorted(perm)
            for mid_idx in range(len(sorted_perm)):
                left = sorted_perm[:mid_idx]
                right = sorted_perm[mid_idx + 1:]
                if len(left) == len(right):
                    candidate = left + [sorted_perm[mid_idx]] + list(reversed(right))
                    palindrome = ''.join(candidate)
                    if palindrome == palindrome[::-1]:
                        palindrome_set.add(palindrome)
    return palindrome_set