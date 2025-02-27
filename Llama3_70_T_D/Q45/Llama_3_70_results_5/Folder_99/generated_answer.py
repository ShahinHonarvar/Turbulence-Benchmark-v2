from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            if len(set(p)) == 1 or p == p[::-1]:
                palindrome = ''.join(p)
                if len(palindrome) >= 3:
                    palindromes.add(palindrome)
    return palindromes