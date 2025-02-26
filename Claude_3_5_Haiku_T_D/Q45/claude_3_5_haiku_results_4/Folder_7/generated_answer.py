from itertools import permutations

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[1:10] if char.isalpha()]
    palindrome_set = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            candidate = ''.join(perm)
            if len(set(candidate)) >= 7 and candidate == candidate[::-1]:
                palindrome_set.add(candidate)
    return palindrome_set