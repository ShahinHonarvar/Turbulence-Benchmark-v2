from itertools import combinations, permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    chars = [c for c in s if c.isalpha()]
    if len(chars) >= 6:
        result = set()
        for perm in permutations(chars, 6):
            for sub in combinations(range(6), 3):
                left = perm[sub[0]:sub[1]]
                right = perm[sub[1]:sub[2]]
                word = ''.join(left + right)
                if is_palindrome(word):
                    result.add(word)
        return result
    else:
        return set()