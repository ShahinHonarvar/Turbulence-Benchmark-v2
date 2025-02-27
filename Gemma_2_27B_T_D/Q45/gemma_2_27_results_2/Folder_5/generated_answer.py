from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([c for c in text[4:9] if c.isalpha()]).lower()
    palindromes = set()
    for r in range(len(letters) // 2, 0, -1):
        for p in permutations(letters, r):
            palindrome = ''.join(p) + ''.join(p[::-1])
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes