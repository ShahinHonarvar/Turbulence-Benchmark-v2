from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    letters = [c.lower() for c in s[3:6] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = list(perm)
            mid = len(candidate) // 2
            if len(candidate) % 2 == 0:
                left = candidate[:mid]
                right = candidate[mid:]
                right.reverse()
            else:
                left = candidate[:mid]
                right = candidate[mid + 1:]
                right.reverse()
            if left == right:
                palindrome = ''.join(candidate)
                if len(palindrome) >= 3:
                    palindromes.add(palindrome)
    return palindromes