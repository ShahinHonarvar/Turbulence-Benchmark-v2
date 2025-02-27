import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.isalpha()]
    palindromes = set()
    for r in range(2, len(letters) + 1):
        for combination in itertools.combinations(letters, r):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation)
                if palindrome == palindrome[::-1] and len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes