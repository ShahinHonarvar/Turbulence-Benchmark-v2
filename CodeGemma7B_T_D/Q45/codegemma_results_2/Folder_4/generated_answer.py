from itertools import permutations

def palindromes_between_indices(word):

    def is_palindrome(word):
        return word == word[::-1]
    word = word.lower()
    setence = set()
    for permutation in permutations(word[3:10]):
        if is_palindrome(''.join(permutation)):
            setence.append(''.join(permutation))
    if not setence:
        return set()
    return setence