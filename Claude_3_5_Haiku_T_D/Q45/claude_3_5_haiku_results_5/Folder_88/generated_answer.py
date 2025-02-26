from itertools import permutations

def palindromes_between_indices(s):
    letters = s[3:8]
    english_letters = [char.lower() for char in letters if char.isalpha()]
    if len(english_letters) < 6:
        return set()
    palindrome_set = set()
    for perm in set(permutations(english_letters, 6)):
        for i in range(6):
            candidate = perm[:i] + tuple(reversed(perm[i:]))
            palindrome = ''.join(candidate)
            if len(set(palindrome)) == 1:
                continue
            if palindrome == palindrome[::-1]:
                palindrome_set.add(palindrome)
    return palindrome_set