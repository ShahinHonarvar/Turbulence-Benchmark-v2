from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        word = word.lower()
        return word == word[::-1]
    s = s[5:10].lower()
    letters_only = ''.join(filter(str.isalpha, s))
    palindromes_set = set()
    for length in range(5, len(letters_only) + 1):
        for perm in permutations(letters_only, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes_set.add(candidate)
    return palindromes_set