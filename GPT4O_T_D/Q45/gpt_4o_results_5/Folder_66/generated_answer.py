from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substr = ''.join(filter(str.isalpha, s[:6])).lower()
    palindromes = set()
    if len(substr) >= 5:
        all_perms = [''.join(p) for p in permutations(substr, len(substr))]
        for perm in all_perms:
            for i in range(5, len(perm) + 1):
                if is_palindrome(perm[:i]):
                    palindromes.add(perm[:i])
    return palindromes