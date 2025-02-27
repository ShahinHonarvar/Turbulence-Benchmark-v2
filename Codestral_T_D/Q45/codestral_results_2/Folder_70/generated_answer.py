from itertools import permutations

def palindromes_between_indices(string):

    def is_palindrome(s):
        return s == s[::-1]
    string = string[1:7].lower()
    palindromes = set()
    for length in range(4, len(string) + 1):
        for perm in permutations(string, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes