from itertools import combinations, permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join(filter(str.isalpha, s[7:10].lower()))
    result = set()
    for r in range(4, len(substring) + 1):
        for comb in combinations(substring, r):
            for perm in permutations(comb):
                word = ''.join(perm)
                if is_palindrome(word):
                    result.add(word)
    return result