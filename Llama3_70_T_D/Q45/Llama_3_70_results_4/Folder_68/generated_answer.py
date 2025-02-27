import itertools
from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = [char for char in s if char in ascii_lowercase]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combo in itertools.combinations(letters, length):
            for perm in itertools.permutations(combo):
                word = ''.join(perm)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes