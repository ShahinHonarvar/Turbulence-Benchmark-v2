from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:6] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) * 2 + 1):
        for perm in set(permutations(letters, length // 2)):
            half = list(perm)
            if length % 2 == 0:
                palindrome = half + half[::-1]
            else:
                for mid in letters:
                    palindrome = half + [mid] + half[::-1]
            palindrome_str = ''.join(palindrome)
            if len(palindrome_str) >= 4 and palindrome_str == palindrome_str[::-1]:
                palindromes.add(palindrome_str)
    return palindromes