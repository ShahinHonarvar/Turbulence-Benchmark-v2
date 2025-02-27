from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def generate_permutations(s, l, r):
        if l == r:
            return {s[l]}
        permutations = set()
        for i in range(l, r + 1):
            for perm in generate_permutations(s, l, i - 1):
                permutations.add(perm + s[i])
            for perm in generate_permutations(s, i + 1, r):
                permutations.add(s[i] + perm)
        return permutations
    s = s.lower()
    if len(s) < 9:
        return set()
    s = s[6:9]
    english_letters = {chr(i) for i in range(ord('a'), ord('z') + 1)}
    s = ''.join((c for c in s if c in english_letters))
    if len(s) < 4:
        return set()
    permutations = generate_permutations(s, 0, len(s) - 1)
    palindromes = {perm for perm in permutations if is_palindrome(perm)}
    return palindromes