from itertools import permutations

def palindromes_between_indices(s: str) -> set:
    s = s[4:10].lower()
    palindromes = set()
    for length in range(4, len(s) + 1):
        for perm in permutations(s, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes