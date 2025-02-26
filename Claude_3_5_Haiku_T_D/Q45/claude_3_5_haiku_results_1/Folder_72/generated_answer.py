from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    palindrome_set = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for combo in set(permutations(perm)):
                test_str = ''.join(combo)
                if test_str == test_str[::-1]:
                    palindrome_set.add(test_str)
    return palindrome_set