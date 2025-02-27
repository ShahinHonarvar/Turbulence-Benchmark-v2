from itertools import permutations

def palindromes_between_indices(s):
    substr = s[6:9].lower()
    eng_letters = ''.join((c for c in substr if c.isalpha()))
    if len(eng_letters) < 2:
        return set()
    palindromes = set()
    for r in range(4, len(eng_letters) + 1):
        for perm in permutations(eng_letters, r):
            if perm == perm[::-1]:
                palindrome = ''.join(perm)
                for i in range(len(eng_letters) - r + 1):
                    palindromes.add(palindrome)
    return palindromes