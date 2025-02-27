from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:5] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        for i in range(1, len(letters)):
            palindrome = ''.join(perm[:i] + perm[:i][::-1])
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes