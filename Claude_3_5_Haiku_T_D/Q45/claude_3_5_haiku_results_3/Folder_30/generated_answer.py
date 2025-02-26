from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:5] if char.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm) // 2 + 1):
            candidate = list(perm)
            left = candidate[:i]
            right = list(reversed(candidate[:i]))
            mid = candidate[i:len(perm) - i]
            palindrome = left + mid + right
            palindrome_str = ''.join(palindrome)
            if len(palindrome_str) >= 4:
                palindromes.add(palindrome_str)
    return palindromes