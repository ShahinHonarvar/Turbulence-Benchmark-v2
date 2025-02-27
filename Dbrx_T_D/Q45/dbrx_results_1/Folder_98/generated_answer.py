from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def generate_permutations(s):
        if len(s) == 1:
            return [s]
        permutations = []
        for i in range(len(s)):
            for perm in generate_permutations(s[:i] + s[i + 1:]):
                permutations.append(s[i] + perm)
        return permutations
    english_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    s = s.lower()
    letters_in_range = [c for c in s[3:6] if c in english_letters]
    permutations = generate_permutations(''.join(letters_in_range))
    return {perm for perm in permutations if is_palindrome(perm) and len(perm) >= 4}