from itertools import permutations

def palindromes_between_indices(s):
    subset = s[6:10].lower()
    letters = [char for char in subset if char.isalpha()]
    if len(letters) < 4:
        return set()
    palindrome_set = set()
    for r in range(4, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            for possible_palindrome in set(permutations(perm + perm[::-1])):
                candidate = ''.join(possible_palindrome)
                if len(candidate) >= 4 and candidate == candidate[::-1]:
                    palindrome_set.add(candidate)
    return palindrome_set