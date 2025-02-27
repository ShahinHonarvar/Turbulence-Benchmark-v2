import itertools

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    letters = [c for c in s[4:10] if c.isalpha()]
    letters = ''.join(letters).lower()
    combinations = set()
    for length in range(3, len(letters) + 1):
        for combo in itertools.permutations(letters, length):
            palindrome = ''.join(combo)
            if is_palindrome(palindrome):
                combinations.add(palindrome)
    return combinations