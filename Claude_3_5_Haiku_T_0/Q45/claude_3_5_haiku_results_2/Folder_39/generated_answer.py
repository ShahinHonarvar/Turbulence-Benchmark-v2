from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = list(perm)
            mid = len(candidate) // 2
            for j in range(mid):
                candidate[len(candidate) - 1 - j] = candidate[j]
            palindrome = ''.join(candidate)
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes