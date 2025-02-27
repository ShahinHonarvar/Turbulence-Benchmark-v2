from itertools import permutations

def palindromes_between_indices(s):
    s = s[:4].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for p1 in permutations(letters, 2):
        for p2 in permutations(letters, 2):
            palindrome = ''.join(p1 + p2)
            if palindrome == palindrome[::-1] and len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes