from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:10] if c.isalpha()]
    palindrome_set = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            perm_list = list(perm)
            if len(set(perm_list)) < 2:
                continue
            for p in set(permutations(perm_list)):
                p_str = ''.join(p)
                if p_str == p_str[::-1]:
                    palindrome_set.add(p_str)
    return palindrome_set