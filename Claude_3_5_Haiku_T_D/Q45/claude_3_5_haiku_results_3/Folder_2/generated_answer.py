from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:6] if char.isalpha()]
    palindrome_set = set()
    for perm_length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, perm_length)):
            for i in range(len(perm) - perm_length + 1):
                subset = perm[i:i + perm_length]
                if len(subset) >= 6:
                    candidate = subset + subset[::-1][1:]
                    palindrome = ''.join(candidate)
                    if palindrome == palindrome[::-1]:
                        palindrome_set.add(palindrome)
    return palindrome_set