import itertools
import string

def palindromes_between_indices(s):
    s = s[1:10].lower()
    letters = [char for char in s if char in string.ascii_lowercase]
    palindromes = set()
    for combo in itertools.combinations_with_replacement(letters, 7):
        for perm in itertools.permutations(combo):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes