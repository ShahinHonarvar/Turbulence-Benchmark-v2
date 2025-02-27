import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[6:10] if c.isalpha()]
    combinations = set(itertools.permutations(letters, r=4))
    palindromes = set()
    for combo in combinations:
        if combo == combo[::-1]:
            palindrome = ''.join(combo).lower()
            palindromes.add(palindrome)
    return palindromes