import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:9] if char.isalpha()]
    if len(letters) < 7:
        return set()
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes