from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[0:5] if c.isalpha()]
    palindrome_set = set()
    for perm_length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, perm_length)):
            perm_list = list(perm)
            if len(perm_list) >= 3:
                for i in range(len(perm_list)):
                    temp_perm = perm_list[i:] + perm_list[:i]
                    if temp_perm == temp_perm[::-1]:
                        palindrome_set.add(''.join(temp_perm))
    return palindrome_set