from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:5] if c.isalpha()]
    if len(letters) < 5:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = list(perm)
            for j in range(len(candidate) // 2):
                candidate[j], candidate[-(j + 1)] = (candidate[-(j + 1)], candidate[j])
            palindrome = ''.join(candidate)
            if palindrome == ''.join(candidate):
                palindrome_set.add(palindrome)
    return {pal for pal in palindrome_set if len(pal) >= 5}