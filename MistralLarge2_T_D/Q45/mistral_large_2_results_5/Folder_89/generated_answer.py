import itertools

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[5:10] if c.isalpha()]).lower()
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes