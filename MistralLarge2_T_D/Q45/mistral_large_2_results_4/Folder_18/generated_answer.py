import itertools

def palindromes_between_indices(s):
    chars = [c for c in s[1:7] if c.isalpha()]
    chars = ''.join(chars).lower()
    palindromes = set()
    for length in range(3, len(chars) + 1):
        for perm in itertools.permutations(chars, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes