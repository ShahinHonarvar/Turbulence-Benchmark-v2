import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:6].lower() if c.isalpha()]
    letters_set = set(letters)
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes