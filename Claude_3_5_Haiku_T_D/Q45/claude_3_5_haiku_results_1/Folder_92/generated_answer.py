from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    letters = [c.lower() for c in s[4:8] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = list(perm)
            left = candidate[:i + 1]
            right = candidate[i + 1:]
            full_palindrome = left + list(reversed(right))
            if len(full_palindrome) >= 4:
                palindrome_str = ''.join(full_palindrome)
                if palindrome_str == palindrome_str[::-1]:
                    palindromes.add(palindrome_str)
    return palindromes