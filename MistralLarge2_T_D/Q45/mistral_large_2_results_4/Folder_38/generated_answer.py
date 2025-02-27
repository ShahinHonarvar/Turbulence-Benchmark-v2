from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[3:9] if c.isalpha()]
    palindromes = set()
    for length in range(5, len(chars) + 1):
        for perm in permutations(chars, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes