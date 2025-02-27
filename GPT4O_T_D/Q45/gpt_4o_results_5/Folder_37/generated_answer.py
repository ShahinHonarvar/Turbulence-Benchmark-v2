from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        for i in range(len(perm_str) - 4):
            substr = perm_str[i:i + 5]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes