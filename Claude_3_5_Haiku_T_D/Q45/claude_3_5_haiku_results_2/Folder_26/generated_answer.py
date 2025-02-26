from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:7] if c.isalpha()]
    palindrome_set = set()
    if len(letters) < 3:
        return palindrome_set
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 2, len(perm) + 1):
                subset = list(perm[i:j])
                if len(subset) >= 3:
                    palindrome = subset + subset[::-1]
                    palindrome_str = ''.join(palindrome)
                    if palindrome_str == palindrome_str[::-1]:
                        palindrome_set.add(palindrome_str)
    return palindrome_set