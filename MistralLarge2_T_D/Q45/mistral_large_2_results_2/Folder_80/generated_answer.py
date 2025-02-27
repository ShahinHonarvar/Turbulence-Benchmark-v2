from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:9] if c.isalpha()]
    lower_letters = [c.lower() for c in letters]
    palindromes = set()
    for length in range(7, len(lower_letters) + 1):
        for perm in permutations(lower_letters, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes