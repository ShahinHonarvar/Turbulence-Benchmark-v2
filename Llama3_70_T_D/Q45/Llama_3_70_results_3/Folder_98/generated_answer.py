from itertools import permutations, combinations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[3:6] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combo in combinations(letters, length):
            for perm in permutations(combo):
                if perm == perm[::-1]:
                    palindrome = ''.join(perm)
                    palindromes.add(palindrome)
    return palindromes