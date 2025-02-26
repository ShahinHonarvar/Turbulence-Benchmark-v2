from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:5] if char.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) * 2 + 1):
        for perm in set(permutations(letters, length // 2)):
            half = list(perm)
            if length % 2 == 0:
                candidate = half + half[::-1]
            else:
                candidate = half + [half[-1]] + half[::-1]
            palindrome = ''.join(candidate)
            if len(palindrome) >= 5:
                palindromes.add(palindrome)
    return palindromes