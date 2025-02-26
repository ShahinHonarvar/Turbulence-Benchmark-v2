from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[:8] if c.isalpha()))
    if len(letters) < 7:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters, 7)):
        for i in range(4):
            candidate = list(perm)
            left = candidate[:3 - i]
            right = candidate[3 - i:]
            palindrome_candidate = left + [perm[3]] + list(reversed(right))
            palindrome = ''.join(palindrome_candidate)
            if palindrome == palindrome.lower() and palindrome == palindrome[::-1]:
                unique_palindromes.add(palindrome)
    return unique_palindromes