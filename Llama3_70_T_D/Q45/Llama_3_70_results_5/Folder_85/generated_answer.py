from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s_between = s[2:9]
    english_letters = [c for c in s_between if c.isalpha()]
    if len(english_letters) < 7:
        return set()
    palindromes = set()
    for perm in permutations(english_letters, 7):
        first_half = ''.join(perm[:4])
        if first_half == first_half[::-1]:
            palindrome = first_half + ''.join(perm[4:]) + first_half[::-1]
            palindromes.add(palindrome)
    return palindromes