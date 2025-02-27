import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:8] if c.isalpha() and c.lower() in 'abcdefghijklmnopqrstuvwxyz']
    unique_letters = set(letters)
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                palindrome = ''.join(perm).lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes