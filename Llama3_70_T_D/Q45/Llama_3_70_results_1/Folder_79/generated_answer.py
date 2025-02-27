from itertools import combinations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[1:8] if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in combinations(letters, r):
            for i in range(r // 2 + 1):
                palindrome = combo[:i] + combo[-i - 1:-i + len(combo) - 2 * i - 1:-1] + combo[i:]
                palindromes.add(''.join(palindrome))
    return palindromes