import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:7] if c.isalpha()]
    unique_letters = set(letters)
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for comb in itertools.combinations_with_replacement(unique_letters, r):
            for perm in itertools.permutations(comb):
                palindrome = ''.join(perm)
                if palindrome.casefold() == palindrome.casefold()[::-1]:
                    palindromes.add(palindrome)
    return palindromes