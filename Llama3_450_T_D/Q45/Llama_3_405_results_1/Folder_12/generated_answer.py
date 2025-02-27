import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:9] if char.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for permutation in itertools.permutations(letters, r):
            palindrome = ''.join(permutation)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes