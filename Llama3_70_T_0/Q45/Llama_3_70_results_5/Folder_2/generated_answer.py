from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        for i in range(len(p) // 2 + 1):
            palindrome = ''.join(p[:i] + p[i:-i - 1][::-1] + p[-i:])
            if len(palindrome) >= 6:
                palindromes.add(palindrome)
    return palindromes