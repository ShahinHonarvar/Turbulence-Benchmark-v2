from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substring = s[4:9].lower()
    english_letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for perm in permutations(english_letters):
        mid = len(perm) // 2
        if perm[:mid] == perm[-1:-(mid + 1):-1]:
            potential_palindrome = ''.join(perm)
            if len(potential_palindrome) >= 4:
                palindromes.add(potential_palindrome)
    return palindromes