from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:7] if char.isalpha()]
    if len(letters) < 4:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = list(perm)
            candidate.extend(list(reversed(candidate[:i])))
            palindrome = ''.join(candidate)
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindrome_set.add(palindrome)
    return palindrome_set