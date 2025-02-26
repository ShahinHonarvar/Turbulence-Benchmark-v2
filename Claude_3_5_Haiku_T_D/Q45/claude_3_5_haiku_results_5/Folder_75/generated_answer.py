from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:5] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = list(perm)
            mid = candidate[i]
            del candidate[i]
            candidate.sort()
            left = candidate[:len(candidate) // 2]
            right = candidate[len(candidate) // 2:]
            right.reverse()
            palindrome = left + [mid] + right
            palindrome = ''.join(palindrome)
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes