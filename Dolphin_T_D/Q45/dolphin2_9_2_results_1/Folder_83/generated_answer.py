from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for perm in permutations(s[2:10], len(s[2:10])):
        for i in range(len(perm)):
            for j in range(i + 6, len(perm)):
                if is_palindrome(perm[i:j + 1]):
                    palindromes.add(perm[i:j + 1].lower())
    return palindromes