from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    if len(s) >= 3:
        for perm in permutations(s):
            for i in range(len(perm) // 2 + 1):
                palindrome = ''.join(perm[:i] + list(reversed(perm[:i])) + perm[i:])
                if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes