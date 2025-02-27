from itertools import permutations as p

def palindromes_between_indices(s):
    s = s[4:9]
    palindromes = set()
    for perm in p(s, len(s)):
        for word in p(perm, len(word) // 2):
            palindrome = ''.join(word) + ''.join(reversed(word[::-1]))
            if len(palindrome) >= 4:
                palindromes.add(palindrome.lower())
    return palindromes