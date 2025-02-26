from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6] if c.isalpha()]
    palindrome_set = set()
    if len(letters) < 3:
        return palindrome_set
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 1, len(perm)):
                test_perm = list(perm)
                test_perm[i], test_perm[j] = (test_perm[j], test_perm[i])
                if len(test_perm) >= 3:
                    palindrome = ''.join(test_perm + test_perm[::-1])
                    if palindrome == palindrome[::-1]:
                        palindrome_set.add(palindrome)
    return palindrome_set