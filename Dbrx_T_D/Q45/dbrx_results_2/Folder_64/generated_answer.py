from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def get_permutations(s):
        if len(s) == 1:
            return [s]
        permutations = set()
        for i in range(len(s)):
            for perm in get_permutations(s[:i] + s[i + 1:]):
                permutations.add(perm + s[i])
        return permutations
    s = s.lower()
    if len(s) < 5 or 'a' not in s[4:10] or 'z' not in s[4:10]:
        return set()
    english_letters = {chr(i) for i in range(ord('a'), ord('z') + 1)}
    substring = ''.join((c for c in s[4:10] if c in english_letters))
    if len(substring) < 5:
        return set()
    perms = get_permutations(substring)
    palindromes = set(filter(is_palindrome, perms))
    return {palindrome for palindrome in palindromes if len(palindrome) >= 5}