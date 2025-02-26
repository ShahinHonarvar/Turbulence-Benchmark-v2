from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:10] if char.isalpha()]
    palindrome_set = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            perm_list = list(perm)
            for i in range(length // 2):
                if perm_list[i] != perm_list[length - 1 - i]:
                    break
            else:
                palindrome_set.add(''.join(perm_list))
    return palindrome_set