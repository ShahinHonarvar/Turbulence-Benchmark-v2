def palindromes_between_indices(s):
    letters = [c for c in s.lower() if c.isalpha()]
    for permutation in itertools.permutations(letters, 6):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            return set(palindromes_between_indices(s)[0])
    return set()