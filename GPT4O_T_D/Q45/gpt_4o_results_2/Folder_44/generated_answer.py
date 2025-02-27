from itertools import permutations

def palindromes_between_indices(s):
    substr = s[2:8].lower()
    letters = [c for c in substr if c.isalpha()]
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            joined = ''.join(perm)
            if joined == joined[::-1]:
                palindromes.add(joined)
    return palindromes